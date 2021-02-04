// var score = document.getElementById('score')
// var clickId = document.getElementById('click')
// var counter = 0
// clickId.addEventListener('click', function () {
//     counter++;
//     score.textContent='Score: '+counter
// })
//
// var reset =
// document.getElementById('reset')
// reset.onclick = function() {
//   counter = 0;
//   score.textContent = "Score: " + counter;
// };



var button = document.getElementById('click'),
    count = 0;
button.onclick = function() {
    count += 1;
  button.innerHTML = "click to count: " + count;
};
var reset =
document.getElementById('reset')
reset.onclick = function() {
  count = 0;
  button.innerHTML = "click to count: " + count;
};
