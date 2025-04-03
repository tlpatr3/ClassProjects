// let dogBreeds = ["Rotweiler", "Doberman", "Beagle", "Poodle"]

// let dog = {breed : "Beagle", age: 5, color: "brown"}

// for (key in dog) {
//     console.log(key + " " + dog [key])
// }



// a while loop checks the condition before it executes, but a do while loop will execute once and then check//

// let counter = 100;
// do {
//     console.log(counter);
//     counter++;
// } while (counter <= 5);

// this will print 100 once and then stop because the condition is false//

// generally, for loop is used when you know how many times you want the loop to repeat, use for of loop when you want to iterate through the array, for in loop is for doing the same with an object//
// while loop will only trigger if the condition is true and will continue as long as it is true; do while loop will always trigger at least once, even if false//

// let age = 67;
// let felon = false;
// let canVote;
// // if (age >= 18 && felonStatus === false) {
// //     console.log("You can vote");
// // } else {
// //     console.log("You cannot vote");
// // }
// // == for value, === for value and type, so either would work in this case//
// //OR//
// age >= 18 && !felon == false ? canVote = true : canVote = false;
// console.log (canVote)
// ternary operator is a shorthand for if else statements//


let animal = 'chicken';
switch(animal) {
    case 'pig':
        console.log('bacon');
        break;
    case 'cow':
        console.log('steak');
        break;
    default:
        console.log('no food');
        break;
}
// switch statements are used when you have multiple conditions to check, and it is cleaner than using multiple if else statements//
