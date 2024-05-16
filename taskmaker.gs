function main() {
  // console log and get all tasklists
  let taskLists = listTaskLists();
  
  // add a task to my tasks
  //addTask(taskLists.items[0].id);

  // mastertask task id is RXRhREhkdEZkR3FURkdhcA
  masterId = 'RXRhREhkdEZkR3FURkdhcA';
  whereIsIt = 'NWo4am1WVkF3YWJFM3l1OA';
  pickOneFromDescAndAdd(masterId, whereIsIt);
}

/**
 * Lists the titles and IDs of tasksList.
 * @see https://developers.google.com/tasks/reference/rest/v1/tasklists/list
 */
function listTaskLists() {
  try {
    // Returns all the authenticated user's task lists.
    const taskLists = Tasks.Tasklists.list();
    // If taskLists are available then print all tasklists.
    if (!taskLists.items) {
      console.log('No task lists found.');
      return;
    }
    // Print the tasklist title and tasklist id.
    for (let i = 0; i < taskLists.items.length; i++) {
      const taskList = taskLists.items[i];
      console.log('Task list with title "%s" and ID "%s" was found.', taskList.title, taskList.id);
      listTasks(taskList.id);
    }
    return taskLists;
  } catch (err) {
    // TODO (developer) - Handle exception from Task API
    console.log('Failed with an error %s ', err.message);
  }
}

/**
 * Lists task items for a provided tasklist ID.
 * @param  {string} taskListId The tasklist ID.
 * @see https://developers.google.com/tasks/reference/rest/v1/tasks/list
 */
function listTasks(taskListId) {
  try {
    // List the task items of specified tasklist using taskList id.
    const tasks = Tasks.Tasks.list(taskListId);
    // If tasks are available then print all task of given tasklists.
    if (!tasks.items) {
      console.log('No tasks found.');
      return;
    }
    // Print the task title and task id of specified tasklist.
    for (let i = 0; i < tasks.items.length; i++) {
      const task = tasks.items[i];
      console.log('Task with title "%s" and ID "%s" was found.', task.title, task.id);
    }
  } catch (err) {
    // TODO (developer) - Handle exception from Task API
    console.log('Failed with an error %s', err.message);
  }
}

/**
 * Adds a task to a tasklist.
 * @param {string} taskListId The tasklist to add to.
 * @see https://developers.google.com/tasks/reference/rest/v1/tasks/insert
 */
function addTask(taskListId) {
  // Task details with title and notes for inserting new task
  const MILLIS_PER_DAY = 1000 * 60 * 60 * 24;
  const now = new Date();
  const tomorrowDate = new Date(now.getTime() + MILLIS_PER_DAY);
  const tomorrow = Utilities.formatDate(tomorrowDate, 'EDT', "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");

  let task = {
    title: 'Pick up dry cleaning',
    notes: 'Remember to get this done!',
    due: tomorrow
  };
  try {
    // Call insert method with taskDetails and taskListId to insert Task to specified tasklist.
    task = Tasks.Tasks.insert(task, taskListId);
    // Print the Task ID of created task.
    console.log('Task with ID "%s" was created.', task.id);
  } catch (err) {
    // TODO (developer) - Handle exception from Tasks.insert() of Task API
    console.log('Failed with an error %s', err.message);
  }
}

// load from master task its description and pick one of the lines to add as a task due today
function pickOneFromDescAndAdd(taskId, fromThisListId) {
  try {
    // get today date
    const todayDate = new Date();
    const today = Utilities.formatDate(todayDate, 'EDT', "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");

    // get the master task's description
    let task = Tasks.Tasks.get(fromThisListId, taskId);
    let description = task.notes;

    // pick one line from it at random
    let lines = description.split('\n');
    let theOne = lines[Math.floor(Math.random() * lines.length)]

    // create a new task with it
    let newTask = {
    title: theOne,
    due: today
    };

    // add it to the Repeat List
    // Call insert method with taskDetails and taskListId to insert Task to specified tasklist.
    createdTask = Tasks.Tasks.insert(newTask, fromThisListId);
    // Print the Task ID of created task.
    console.log('Task with ID "%s" was created.', createdTask.id);
    // console.log('Task with ID "%s" has description "%s.', task.id, description);

  } catch (err) {
    console.log('Failed with an error %s', err.message);
  }
}

// // pull quotes from internet
// function pullQuotes() {

// }
