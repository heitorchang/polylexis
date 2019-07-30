var title = "Useful phrases (remember to capitalize the first letter)";
                
var original_order = questions.slice();
var all_done = "Fim! Clique na flecha ou digite Enter para voltar";

var span_prompt = document.getElementById("prompt");
var input_textbox = document.getElementById("textbox");

var current = 0;
var num_questions = questions.length;

var advance_button = document.getElementById("advance");
var reveal_button = document.getElementById("reveal");
var backend_button = document.getElementById("backend");

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

function hide(elemId) {
  document.getElementById(elemId).style.display = "none";
}

function show(elemId) {
  document.getElementById(elemId).style.display = "inline";
}

document.getElementById("inorder").onclick = function () {
  questions = original_order.slice();
  current = 0;
  setup_question(current);
  show("reveal");
  hide("advance");
  hide("backend");
  input_textbox.focus();
}

document.getElementById("shuffled").onclick = function () {
  shuffleArray(questions);
  current = 0;
  setup_question(current);
  show("reveal");
  hide("advance");
  hide("backend");
  input_textbox.focus();
}

function notice(msg) {
  if (msg === "") {
    msg = "&nbsp;";
  }
  span_prompt.innerHTML = msg;
}

function setup_question(idx) {
  span_prompt.innerText = questions[current].prompt.join(" / ");
  span_cur_q.innerText = current + 1;
  input_textbox.value = "";
  input_textbox.focus();
  show("reveal");
  hide("advance");
}

function advance(user_ans) {
  // check if answer is correct and advance current if true
  user_ans = user_ans.trim();
  if (questions[current].answer.indexOf(user_ans) >= 0) {
    current += 1;
    // notice("");
    advance_button.style.display = "none";
    reveal_button.style.display = "inline";
    input_textbox.value = "";
    if (current === num_questions) {
      span_prompt.innerText = all_done;
      show("backend");
      hide("reveal");
      backend_button.focus();
    } else {
      setup_question(current);
    }
  }
}

advance_button.onclick = function () {
  advance(input_textbox.value);
}

backend_button.onclick = function () {
  window.location.href = './';
}

document.getElementById("reveal").onclick = function () {
  input_textbox.value = questions[current].answer[0];
  checkAns(input_textbox.value.trim());
  advance_button.focus();
}

function checkAns(user_ans) {
  // remove extra spaces between words
  user_ans = user_ans.trim();
  user_ans = user_ans.replace(/\s+/g, " ");
  
  if (questions[current].answer.indexOf(user_ans) >= 0) {
    if (questions[current].answer.length > 1) {
      var all_accepted = " (" + questions[current].answer.join(" / ") + ")";
    } else {
      var all_accepted = "";
    }
    notice('<span style="color: #393;"><b>Correto!</b></span> ' + all_accepted);
    show("advance");
    hide("reveal");
  } else {
    span_prompt.innerText = questions[current].prompt.join(" / ");
    show("reveal");
    hide("advance");
  }
}

setup_question(current);

document.getElementById("textbox").onkeyup = function (e) {
  if ((input_textbox.value.indexOf('$') >= 0 || input_textbox.value.indexOf('=') >= 0) && current < num_questions) {
    input_textbox.value = questions[current].answer[0];
  }
  if (current < num_questions) {
    var user_ans = input_textbox.value;
    
    checkAns(user_ans);
    
    if (e.keyCode === 13) {
      advance(user_ans);
    }
  } else {
    if (span_prompt.innerText === all_done && e.keyCode === 13) {
      window.location.href = './';
    }
  }
}

// see if mobile input method changed (added accent/converted a character)
$("#textbox").bind("propertychange change input paste", function () {
  if (current < num_questions) {
    var user_ans = input_textbox.value;
    user_ans = user_ans.trim();

    checkAns(user_ans);
  }  
});

document.getElementById("swap").onclick = function () {
  for (var i = 0; i < questions.length; i++) {
    var temp = questions[i].prompt;
    questions[i].prompt = questions[i].answer;
    questions[i].answer = temp;
  }
  setup_question(current);
}
