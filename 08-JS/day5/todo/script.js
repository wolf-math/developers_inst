const tasks = [];

function listTasks() {
  todoList = document.getElementById('todoList');
  todoList.innerHTML = '';
  tasks.forEach((task, index) => {
    const todo = document.createElement('li');
    todo.className = 'list-group-item';
    todo.innerHTML = `
            <div id="task-${index}" class="lineItem-container">
              <input class="form-check-input check" type="checkbox" >
              <div class="lineItem">${task} <i class="bi bi-trash"></i></div>
            </div>
    `;
    todoList.appendChild(todo);
  });
}

function addTask() {
  const todoItem = document.getElementById('form1');

  todoItem.addEventListener('submit', (e) => {
    e.preventDefault();

    const inputField = todoItem.querySelector('input[type="text"]');
    if (inputField.value.trim() == '') {
      return;
    }
    tasks.push(inputField.value);
    listTasks();
    todoItem.reset();
  });
}

addTask();
