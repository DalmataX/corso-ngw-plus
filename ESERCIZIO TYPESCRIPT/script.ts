const button = document.getElementById("add-button")!;
const input = document.getElementById("todo-input") as HTMLInputElement;
const todoList = document.getElementById("todo-list") as HTMLUListElement;

type TodoItem = {
  id: number;
  task: string;
};

let todoItems: TodoItem[] = [];

function aggiungiTodo(task: string): void {
  const newItem: TodoItem = {
    id: Date.now(),
    task: task,
  };
  todoItems.push(newItem);
  renderizzaTodo();
}

function rimuoviTodo(id: number): void {
  todoItems = todoItems.filter((item) => item.id !== id);
  renderizzaTodo();
}

function renderizzaTodo(): void {
  todoList.innerHTML = "";
  todoItems.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item.task;
    li.addEventListener("click", () => rimuoviTodo(item.id));
    todoList.appendChild(li);
  });
}

button.addEventListener("click", () => {
  if (input.value.trim()) {
    aggiungiTodo(input.value.trim());
    input.value = "";
  }
});
