let allButton = document.getElementById("all").addEventListener("click", (e)=>{
    let todo = document.querySelector("ul").children
    // console.log(todo)
    Array.prototype.forEach.call(todo, (e)=>{
        e.classList.remove("none")
        // console.log(e.classList)
    })
})
let activeButton = document.getElementById("active").addEventListener("click", (e)=>{
    let todo = document.querySelector("ul").children
    // console.log(todo)
    Array.prototype.forEach.call(todo, (e)=>{
        if(e.children[0].classList.contains("notActive")){
            e.classList.add("none")
        } else {
            e.classList.remove("none")
        }
        // console.log(e.children, "line 18")
    })
})
let completeButton = document.getElementById("complete").addEventListener("click", (e)=>{
    let todo = document.querySelector("ul").children
    // console.log(todo)
    Array.prototype.forEach.call(todo, (e)=>{
        if(e.children[0].classList.contains("active")){
            e.classList.add("none")
        } else {
            e.classList.remove("none")
        }
        // console.log(e.children, "line 18")
    })
})

let form = document.getElementById("form")

let items = []

class todo {
    constructor(id = Date.now(), content = "", completed = false){
        this.id = id
        this.content = content
        this.completed = completed
    }
}

function displayLocalStorage(){
    let storage = localStorage.getItem('items');
    // storage = JSON.parse(storage)
    // console.log(storage, "line 20")
    
    if (storage === null || storage.length == 0){
        items = [];
        let storage = localStorage.setItem('items', items);
        // storage = JSON.parse(storage)
        // console.log("line 23")
        let todoList = document.querySelector('ul');
        todoList.innerHTML = '';
        let todoItem = document.createElement('li');
        todoItem.innerHTML = `No more todos!`;
        todoList.appendChild(todoItem);
    } else {
        let storageParsed = storage;
        storageParsed.forEach(function(storageItem){
            // console.log(storageItem, "line 27")
            createItems(storageItem);
        })
    };
};
displayLocalStorage()

form.addEventListener("submit", function(e) {
    e.preventDefault()

    let taskInput = document.getElementById("taskInput").value
    // console.log(taskInput)
    if(taskInput == ""){
        alert("Please enter a valid task.")
    } else {
        let item = new todo()
        item.content = taskInput
        // store task in local storage
        storeItem(item)
        // add task to ul
        createItems(item)
        // clear input value
        document.getElementById("taskInput").value = ''
    }
})

//function to store items in local storage
function storeItem(item){
    // items = JSON.parse(localStorage.getItem('items'))
    items = localStorage.getItem('items')
    items.push(item);
    localStorage.setItem('items', JSON.stringify(items))
    document.getElementById("tasksLeft").innerHTML = `Tasks Left: ${items.length}`
};

//function to display items in the DOM
function createItems(taskInput){
    // console.log(taskInput, "line 63")

    if(document.querySelector('ul').innerHTML == "<li>No more todos!</li>"){
        document.querySelector('ul').innerHTML = ''
    }

    //create a li tag for the element
    let taskItem = document.createElement('li')
    taskItem.classList.add("tasks")
    taskItem.innerHTML = `<button>${taskInput.content}</button><button class="delete-item">X</button>`;
    // console.log(taskItem.children, "line 69")
    if(taskInput.completed == false){
        taskItem.children[0].classList.add("active")
    } else {
        taskItem.children[0].classList.add("notActive")
    }
    taskItem.children[0].addEventListener("click", (e) => {
        let lstorage = localStorage.getItem('items')
        let storage = JSON.parse(lstorage)
        let index = storage.findIndex(i=>i.id == taskInput.id)
        if(storage[index].completed == false){
            storage[index].completed = true
            taskItem.children[0].classList.remove("active")
            taskItem.children[0].classList.add("notActive")
        } else {
            storage[index].completed = false
            taskItem.children[0].classList.remove("notActive")
            taskItem.children[0].classList.add("active")
        }
        localStorage.setItem('items',JSON.stringify(storage))
        // console.log(localStorage.getItem('items'), "line 86")
    })
    taskItem.children[1].addEventListener("click", (e) => {
        let storage = JSON.parse(localStorage.getItem('items'))
        // console.log(storage, "line 99")
        let index = storage.findIndex(i=>i.id == taskInput.id)
        // console.log(index, "line 101")
        storage.splice(index, 1)
        // console.log(storage, "line 103")
        document.querySelector('ul').innerHTML = ''
        localStorage.setItem('items',JSON.stringify(storage))
        // console.log(localStorage.getItem('items'), "line 92")
        displayLocalStorage()
        document.getElementById("tasksLeft").innerHTML = `Tasks Left: ${storage.length}`
    })
    //Display the task item
    let taskList = document.getElementById("tasks")
    taskList.appendChild(taskItem)
};