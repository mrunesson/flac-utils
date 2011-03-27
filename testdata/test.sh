#!/bin/bash


prepare() {
    cp -Ra src test-src
    cp -Ra dst test-dst
    touch test-dst/tag-differ-dst-newer.flac
    touch test-src/tag-differ-src-newer.flac
    touch test-dst/file1.flac
}


clean() {
   rm -rf test-src test-dst
   echo
}


result() {
    echo
    echo Evaluating test:
    testOK=true
    for testfile in `find test-src -type f -name '*.flac' ! -path "*/.svn/*"`
    do
        expectfile=`echo $testfile | sed "s/test-src/expected-result\/$1-src/"`
	#echo $testfile
        ../tools/flac-diff $testfile $expectfile
        if [ $? -ne 0 ] ; then
            testOK=false
        fi
    done
    if $testOK ; then
	echo -e "\tSrc OK"
    else 
	echo -e "\tERROR in src"
    fi

    testOK=true
    for testfile in `find test-dst -type f -name '*.flac' ! -path "*/.svn/*"`
    do
        expectfile=`echo $testfile | sed "s/test-dst/expected-result\/$1-dst/"`
	#echo $testfile
        ../tools/flac-diff $testfile $expectfile
        if [ $? -ne 0 ] ; then
            testOK=false
        fi
    done
    if $testOK ; then
	echo -e "\tDst OK"
    else 
	echo -e "\tERROR in dst"
    fi
}

testNoArgs() {
    echo Test No Arguments
    echo =================
    prepare
    ../tools/flac-sync test-src test-dst
    result noargs
    clean
}

testCopy() {
    echo Test Copy
    echo =========
    prepare
    ../tools/flac-sync -c test-src test-dst
    result copy
    if [ -f test-dst/notflac.txt ] ; then
	echo -e "\t OK"
    else
       	echo -e "\tERROR: Non flac file was not copied."
    fi
    clean
}

testCopyTime() {
    echo Test Copy Time
    echo ==============
    prepare
    ../tools/flac-sync -c -t test-src test-dst
    result copy-time
    clean
}

testCopyTimeBoth() {
    echo Test Copy Time Both
    echo ===================
    prepare
    ../tools/flac-sync -c -t -b test-src test-dst
    result copy-time-both
    clean
}

testBoth() {
    echo Test Both
    echo =========
    prepare
    ../tools/flac-sync -b test-src test-dst
    result both
    clean
}


testOverwrite() {
    echo Test Overwrite
    echo ==============
    prepare
    ../tools/flac-sync -o test-src test-dst
    result overwrite
    clean
}

testTime() {
    echo Test Time
    echo =========
    prepare
    ../tools/flac-sync -t test-src test-dst
    result time
    clean
}


testCopyOnlyFlac() {
    echo Test Copy Only Flac
    echo ===================
    prepare
    ../tools/flac-sync -c --copy-only-flac test-src test-dst
    if [ -f test-dst/notflac.txt ] ; then
       	echo -e "\tERROR: Non flac file copied."
    else
	echo -e "\tOK"
    fi
    clean
}


testNoArgs
testCopy
testCopyTime
testCopyTimeBoth
testBoth
testOverwrite
testTime
testCopyOnlyFlac
