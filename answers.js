// Coding Dojo Online Cohort April 30, 2018
// Karen Clark
//
// Algorithm Book Chapter 1 Assignments

///////////
// Page 16 
///////////

// Setting and Swapping
// Set myNumber to 42. Set myName to your name.
// Now swap myNumber into myName & vice versa
function setAndSwap() {
    var myNumber = 42;
    var myName = 'Karen';
    var temp = myName;
    myName = myNumber;
    myNumber = temp; 

    return;
}

// Print and Count
// Print all integer multiples of 5, from 512 to 4096.
// Afterward, also log how many there were.
function printAndCount() {
    var count = 0;

    for (var i = 512; i < 4097; i++) {
        if (i % 5 === 0) {
            console.log(i);
            count = count + 1;
        }
    }
    console.log(count);
    return count;
}

// Print -52 to 1066
// Print integers from -52 to 1066 using a FOR loop.
function printMinus52To1066() {
    for (i = -52; i < 1067; i++) {
        console.log(i);
    }
    return;
}

// Multiples of Six
// Print multiples of 6 up to 60,000, using a WHILE.
function multipleOfSix() {
    var i = 0;
    while (i < 60001) {
        if (i % 6 == 0) {
            console.log(i);
        }
        i = i + 1;
    }
    return;
}

// Don't Worry, Be Happy
// Create beCheerful(). Within it, console.log
// string "good morning!" Call it 98 times.

function dontWorryBeHappy() {
    var i = 1;
    while (i < 99) {
        console.log("good morning!");
        i = i + 1;
    }
    return;
}

// Counting the Dojo Way
// Print integers 1 to 100. If divisible by 5, print
// "Coding" instead. If by 10, also print " Dojo".
function countingTheDojoWay() {
    for (i = 1; i < 101; i++) {
        if (i % 5 === 0) {
            console.log('Coding');
            if (i % 10 === 0) {
                console.log('Dojo');
            }
        } else {
            console.log(i);
        }
    }
    return;
}

// Multiples of Three - But Not All
// Using FOR, print multiples of 3 from -300 to 0.
// Skip -3 and -6.
function multiplesOfThree() {
    for (i = -301; i < 1; i++) {
        if (i === -6) {
            continue;
        } else if (i === -3) {
            continue;
        } else if ((Math.abs(i)) % 3 === 0) {
            console.log(i);
        } else { 
            continue; 
        }
    }
    return;
}

// What Do You Know?
// Your function will be given an input parameter
// incoming. Please console.log this value.
function whatDoYouKnow(n) {
    console.log(n);
    return;
}

// Printing Integers While
// Print integers from 2000 to 5280, using a WHILE.
function printingIntegersWhile() {
    var i = 2000;
    while (i < 5281) {
        console.log(i);
        i = i + 1;
    }
    return;
}

// Whoa, That Sucker's Huge
// Add odd integers from -300,000 to 300,000, and
// console.log the final sum. Is there a shortcut?
function whoaThatSuckersHuge() {
    var sum = 0;
    for (i = -300000; i < 300001; i++) {
        if (i % 2 != 0) {
            sum = sum + i;
        }
    }
    console.log(sum);
    return sum;
}

// You Say It's Your Birthday
// If 2 given numbers represent your birth month
// and day in either order, log "How did you
// know?", else log "Just another day...."
function youSayItsYourBirthday(a, b) {
    myBirthDay = 2;
    myBirthMonth = 7;
    if (a === myBirthDay || a === myBirthMonth || b === myBirthDay || b === myBirthMonth ) {
        console.log('How did you know?');
    } else {
        console.log('Just another day....');
    }
    return;
}

// Countdown by Fours
// Log positive numbers starting at 2016, counting
// down by fours (exclude 0), without a FOR loop.
function countdownByFours() {
    var n = 2016;
    while (n > 0) {
        if (n % 4 === 0) {
            console.log(n);
        }
        n = n - 1;
    }
    return;
}

// Leap Year
// Write a function that determines whether a given
// year is a leap year. If a year is divisible by four,
// it is a leap year, unless it is divisible by 100.
// However, if it is divisible by 400, then it is.
function isLeapYear(year) {
    if (year % 400 === 0) {
        console.log(year + ' is a leap year!'); 
    } else if (year % 4 === 0) {
        if (year % 100 > 0) {
            console.log(year + ' is a leap year!');
        } 
    } else {
        console.log(year + ' is not a leap year');
    }
    return;
}

// Flexible Countdown
// Based on earlier “Countdown by Fours”, given
// lowNum, highNum, mult, print multiples of mult
// from highNum down to lowNum, using a FOR.
// For (2,9,3), print 9 6 3 (on successive lines)
function flexibleCountdown(lowNum, highNum, mult) {
    for (i = highNum; i > lowNum; i--) {
        if (i % mult === 0) {
            console.log(i);
        }
    }
    return;
}

// The Final Countdown
// Given 4 parameters (param1,param2,param3,param4),
// print the multiples of param1, starting at param2 and extending to param3. 
// One exception: if a multiple is equal to param4, then skip (don’t print) it. 
// Do this using a WHILE. Given (3,5,17,9), print 6,12,15 
/// (which are all of the multiples of 3 between 5 and 17, and excluding the value 9).
function finalCountdown(param1, param2, param3, param4) {
    // param1 = mult, param2 = lowNum, param3 = highNum, param4 = skip it
    var i = param2;
    var counter = 1;

    while (i < param3) {
        if (i % param1 === 0) {
            if (i !== param4) {
                console.log(i);
                // counter += 1;
            }
        }

        i += 1;
    }

    return;
}

///////////////
// END PAGE 16
///////////////

////////////
// Page 20 
////////////

// Countdown

// Print and Return

// First Plus Length

// Values Greater Than Second

// Values Greater Than Second, Generalized

// This Length, That Value

// Fit the First Value

// Fahrenheit to Celsius

// Celsius to Fahrenheit

///////////////
// END PAGE 20
///////////////

///////////
// Page 22
///////////

// Biggie Size

// Previous Lengths

// Print Low, Return High

// Add Seven to Most

// Print One, Return Another

// Reverse Array

// Double Vision

// Outlook: Negative

// Count Positives

// Always Hungry

// Evens and Odds

// Swap Toward the Center

// Increment the Seconds

// Scale the Array

///////////////
// END PAGE 22
///////////////