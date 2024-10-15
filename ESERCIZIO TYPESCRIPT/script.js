var button = document.getElementById("add-button");
var input = document.getElementById("todo-input");
var todoList = document.getElementById("todo-list");
var todoItems = [];
function aggiungiTodo(task) {
  var newItem = {
    id: Date.now(),
    task: task,
  };
  todoItems.push(newItem);
  renderizzaTodo();
}
function rimuoviTodo(id) {
  todoItems = todoItems.filter(function (item) {
    return item.id !== id;
  });
  renderizzaTodo();
}
function renderizzaTodo() {
  todoList.innerHTML = "";
  todoItems.forEach(function (item) {
    var li = document.createElement("li");
    li.textContent = item.task;
    li.addEventListener("click", function () {
      return rimuoviTodo(item.id);
    });
    todoList.appendChild(li);
  });
}
button.addEventListener("click", function () {
  if (input.value.trim()) {
    aggiungiTodo(input.value.trim());
    input.value = "";
  }
});
