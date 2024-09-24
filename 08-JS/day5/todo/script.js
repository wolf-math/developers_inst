const tasks = [];

function listTasks() {
  const todoList = document.getElementById('todoList');
  todoList.innerHTML = '';

  tasks.forEach((task, index) => {
    const todo = document.createElement('li');
    todo.className = 'list-group-item';

    const lineItemContainer = document.createElement('div');
    lineItemContainer.className = 'lineItem-container';
    lineItemContainer.id = `task-${index}`;

    const checkBox = document.createElement('input');
    checkBox.type = 'checkbox';
    checkBox.className = 'form-check-input check';

    const lineItem = document.createElement('div');
    lineItem.className = 'lineItem';
    lineItem.textContent = task.description;

    if (task.completed) {
      checkBox.checked = true;
      lineItem.style.textDecoration = 'line-through';
    } else {
      checkBox.checked = false;
    }

    checkBox.addEventListener('change', (e) => {
      if (e.target.checked) {
        lineItem.style.textDecoration = 'line-through';
        task['completed'] = true;
      } else {
        lineItem.style.textDecoration = 'none';
        task['completed'] = false;
      }
    });

    const trashIcon = document.createElement('i');
    trashIcon.className = 'bi bi-trash trash';

    trashIcon.addEventListener('click', (e) => {
      e.preventDefault();
      removeTask(index);
    });

    lineItemContainer.appendChild(checkBox);
    lineItemContainer.appendChild(lineItem);
    lineItem.appendChild(trashIcon);
    todo.appendChild(lineItemContainer);
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
    tasks.push({ description: inputField.value, isDone: false });
    listTasks();
    todoItem.reset();
  });
}

addTask();

function removeTask(index) {
  tasks.splice(index, 1);
  listTasks();
}

removeTask();
