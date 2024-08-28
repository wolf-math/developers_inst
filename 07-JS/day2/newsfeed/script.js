let user = {
  username: 'JakeTheDog',
  password: 'BestFriendFin'
};

let database = [user];

let newsfeed = [
  {
    username: 'alice',
    timeline: 'Had a great day at the park!'
  },
  {
    username: 'bob',
    timeline: 'Just finished a great workout session.'
  },
  {
    username: 'clarise',
    timeline: 'Watching a new series on Netflix!'
  }
];

document.getElementById('databaseOutput').textContent =
  'Database: ' + JSON.stringify(database);

document.getElementById('newsfeedOutput').textContent =
  'Newsfeed: ' + JSON.stringify(newsfeed);
