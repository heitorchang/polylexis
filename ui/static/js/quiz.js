var title = "Useful phrases (remember to capitalize the first letter)";
                
var original_order = questions.slice();
var all_done = "All done! Press Enter to go back";

var span_prompt = document.getElementById("prompt");
var input_textbox = document.getElementById("textbox");

var current = 0;
var num_questions = questions.length;

document.getElementById("num_q").innerText = num_questions;

var span_cur_q = document.getElementById("cur_q");

function shuffleArray(array) {
  for (var i = array.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}

document.getElementById("showall").onclick = function () {
  var allans_div = document.getElementById("allans");
  if (allans_div.style.display === "none") {
    allans_div.style.display = "inline";
  } else {
    allans_div.style.display = "none";
  }
  document.getElementById("textbox").focus();
}

document.getElementById("inorder").onclick = function () {
  questions = original_order.slice();
  current = 0;
  setup_question(current);
}

document.getElementById("shuffled").onclick = function () {
  shuffleArray(questions);
  current = 0;
  setup_question(current);
}

function debug(msg) {
  document.getElementById("debug").innerText = msg;
}

function notice(msg) {
  if (msg === "") {
    msg = "&nbsp;";
  }
  document.getElementById("notice").innerHTML = msg;
}

function setup_question(idx) {
  span_prompt.innerText = questions[current].prompt.join(" / ");
  span_cur_q.innerText = current + 1;
  notice("");
  input_textbox.value = "";
  input_textbox.focus();
}

setup_question(current);

document.getElementById("textbox").onkeyup = function (e) {
  if (input_textbox.value.indexOf('=') >= 0 && current < num_questions) {
    input_textbox.value = questions[current].answer[0];
  }
  if (current < num_questions) {
    var user_ans = input_textbox.value;

    if (questions[current].answer.indexOf(user_ans) >= 0) {
      if (questions[current].answer.length > 1) {
        var all_accepted = "<br><br>(All accepted answers: " + questions[current].answer.join(" / ") + ")";
      } else {
        var all_accepted = "";
      }
      notice("Correct! Press Enter to continue. " + all_accepted);
    } else {
      notice("");
    }

    if (e.keyCode === 13) {
      // check if answer is correct and advance current if true
      if (questions[current].answer.indexOf(user_ans) >= 0) {
        current += 1;
        notice("");
        input_textbox.value = "";
        if (current === num_questions) {
          span_prompt.innerText = all_done;
          document.getElementById("back").style.display = "inline";
        } else {
          setup_question(current);
        }
      }
    }
  } else {
    if (span_prompt.innerText === all_done && e.keyCode === 13) {
      window.history.back();
    }
  }
}

document.getElementById("swap").onclick = function () {
  for (var i = 0; i < questions.length; i++) {
    var temp = questions[i].prompt;
    questions[i].prompt = questions[i].answer;
    questions[i].answer = temp;
  }
  setup_question(current);
}
