// Playing with Objects
// Karen Clark
// 2018-05-24

var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];

// 1. How would you print/log John's age?
var john = users.find(function(obj) {
    return obj.name == "John";
})
console.log(john.age);

// 2. How would you print/log the name of the first object?
console.log(users[0].name);

// 3. How would you print/log the name and age of each user using a for loop?
for(var i = 0; i < users.length; i++) {
    console.log(users[i].name + " - " + users[i].age);
}

// Other fun stuff I just made up
// Print the names of anyone 30 or younger
var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];

for(var i = 0; i < users.length; i++) {
    if(users[i].age <= 30) {
        console.log("30 or younger: " + users[i].name);
    }
}
