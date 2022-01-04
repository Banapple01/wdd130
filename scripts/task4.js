/* Lesson 4 */

/* DATA */

// Step 1: Declare a new variable to hold information about yourself

// Step 2: Inside of the object, add a property named name with a value of your name as a string

// Step 3: Add another property named photo with a value of the image path and name (used in Task 2) as a string

// Step 4: Add another property named favoriteFoods with a value of an array of your favorite foods as strings ( hint: [] )

// Step 5: Add another property named hobbies with a value of an array of your hobbies as strings

// Step 6: Add another property named placesLived with a value of an empty array

// Step 7: Inside of the empty array above, add a new object with two properties: place and length and values of an empty string

// Step 8: For each property, add appropriate values as strings

// Step 9: Add additional objects with the same properties for each place you've lived

let me = {
    name          : 'Jonathan Wright',
    photo         : 'images\profile_pic.jpg',
    favoriteFoods : ['Chickfila Sandwich', 'soup', 'frenchtoast'],
    hobbies       : ['playing with my sons', 'spending time with my wife', 'video games with my brothers', 'coding'],
    placesLived   : [
        {
            place  : 'CO',
            length : '12 yrs'
        },
        {
            place  : 'MO',
            length : '1 yr'
        }
    ]
};


/* OUTPUT */

// Step 1: Assign the value of the name property (of the object declared above) to the HTML <span> element with an ID of name
document.getElementById('name').textContent = me.name;

// Step 2: Assign the value of the photo property as the src attribute of the HTML <img> element with an ID of photo
document.getElementById('photo').setAttribute('src', me.photo);
document.querySelector('#photo').setAttribute('width', 200)

// Step 3: Assign the value of the name property as the alt attribute of the HTML <img> element with an ID of photo
document.getElementById('photo').setAttribute('alt', me.name);

// Step 4: For each favorite food in the favoriteFoods property, create an HTML <li> element and place its value in the <li> element
let f1 = document.createElement('li');
f1.textContent = me.favoriteFoods[0];

let f2 = document.createElement('li');
f2.textContent = me.favoriteFoods[1];

let f3 = document.createElement('li');
f3.textContent = me.favoriteFoods[2];

// Step 5: Append the <li> elements created above as children of the HTML <ul> element with an ID of favorite-foods
document.querySelector('#favorite-foods').appendChild(f1);
document.querySelector('#favorite-foods').appendChild(f2);
document.querySelector('#favorite-foods').appendChild(f3);

// Step 6: Repeat Step 4 for each hobby in the hobbies property
let h1 = document.createElement('li');
h1.textContent = me.hobbies[0];

let h2 = document.createElement('li');
h2.textContent = me.hobbies[1];

let h3 = document.createElement('li');
h3.textContent = me.hobbies[2];

let h4 = document.createElement('li');
h4.textContent = me.hobbies[3];

// Step 7: Repeat Step 5 using the HTML <ul> element with an ID of hobbies
document.querySelector('#hobbies').appendChild(h1);
document.querySelector('#hobbies').appendChild(h2);
document.querySelector('#hobbies').appendChild(h3);
document.querySelector('#hobbies').appendChild(h4);

// Step 8: For each object in the <em>placesLived</em> property:
// - Create an HTML <dt> element and put its place property in the <dt> element
// - Create an HTML <dd> element and put its length property in the <dd> element
let p1 = document.createElement('dt');
p1.textContent = me.placesLived[0].place;

let pl1 = document.createElement('dd');
pl1.textContent = me.placesLived[0].length;

let p2 = document.createElement('dt');
p2.textContent = me.placesLived[1].place;

let pl2 = document.createElement('dd');
pl2.textContent = me.placesLived[1].length;

// Step 9: Append the HTML <dt> and <dd> elements created above to the HTML <dl> element with an ID of places-lived
document.querySelector('#places-lived').appendChild(p1);
document.querySelector('#places-lived').appendChild(pl1);
document.querySelector('#places-lived').appendChild(p2);
document.querySelector('#places-lived').appendChild(pl2);
