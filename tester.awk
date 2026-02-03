BEGIN { 
    testcase = 0; 
    input_lines = ""; 
    expected = "" 
}

# Start of a new test case
/^input:/ {
    testcase++;
    input_lines = "";
    expected = "";
    next
}

# When we hit output, run the program with the collected input
/^output:/ {
    # Read the next line as expected output
    getline expected;
    
    tmp = "/tmp/input_" testcase ".txt";
    print input_lines > tmp;
    close(tmp);

    cmd = prog " < " tmp;
    result = "";
    
    # Capture program output
    while ((cmd | getline line) > 0) {
        if (result != "") result = result "\n";
        result = result line;
    }
    close(cmd);

    # Clean up whitespace for comparison
    sub(/[ \t\r\n]+$/, "", result);
    sub(/[ \t\r\n]+$/, "", expected);

    if (result == expected) {
        print "Testcase " testcase " PASSED ✅ ";
    } else {
        print "Testcase " testcase " FAILED ❌";
        print "  Input:    " input_lines;
        print "  Expected: " expected;
        print "  Got:      " result;
    }
    next
}

# Collect lines between 'input:' and 'output:'
{
    if (input_lines == "")
        input_lines = $0;
    else
        input_lines = input_lines "\n" $0;
}
