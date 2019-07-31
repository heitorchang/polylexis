var inp = document.getElementById("textbox");
var capson = false;
var accenton = false;

function addLetter(letter) {
  var caretPos = inp.selectionStart;
  var text = inp.value;
  // insert Greek letter, [0] refers to lowercase in keymap's array
  text = text.slice(0, caretPos) + letter + text.slice(caretPos);
  inp.value = text;
  inp.setSelectionRange(caretPos+1, caretPos+1);
  inp.blur();
  capson = false;
  accenton = false;
  showkb();
  checkAns(text);
}

function backspace() {
  var caretPos = inp.selectionStart;
  var newPos = caretPos - 1;
  if (caretPos > 0) {
    var text = inp.value;
    text = text.slice(0, newPos) + text.slice(caretPos);
    inp.value = text;
    inp.setSelectionRange(newPos, newPos);
    inp.blur();
    checkAns(text);
  }
}

function clr() {
  inp.value = "";
  inp.blur();
  checkAns(inp.value);
}

function hl(el) {
  $(el).addClass("hl");
  window.setTimeout(function() {
    $(el).removeClass("hl");
  }, 75);
}

function togglecaps() {
  capson = !capson;
  showkb();
}

function toggleaccent() {
  accenton = !accenton;
  showkb();
}

function showkb() {
  // hide all
  document.getElementById("lowertbl").style.display = "none";
  document.getElementById("lowertblaccent").style.display = "none";
  document.getElementById("capstbl").style.display = "none";
  document.getElementById("capstblaccent").style.display = "none";
  
  // show based on status
  if (!capson && !accenton) {
    active = "lowertbl";
  } else if (!capson && accenton) {
    active = "lowertblaccent";
  } else if (capson && !accenton) {
    active = "capstbl";
  } else if (capson && accenton) {
    active = "capstblaccent";  
  }
  
  document.getElementById(active).style.display = "inline-block";
}
  
