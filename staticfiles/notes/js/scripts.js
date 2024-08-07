const root = document.querySelector(':root');

// setup the color picker function
// when the user inputs a color, reflect it to --textcolor variable in styles.css
function setupColorPicker() {
  const colorPicker = document.querySelector('.textcolor-picker');
  if (!colorPicker) return;

  console.log('All elements detected for color picker');

  colorPicker.addEventListener('input', function() {
    root.style.setProperty('--textcolor', this.value);
    console.log(`colour changed to ${this.value}`);
  })
}

// setup the textsize input function
// when the user inputs an integer, reflect it to --textsize variable in styles.css
function setupTextSizeInputter() {
  let textSizeInputter = document.querySelector('.textsize-input');
  if (!textSizeInputter) return;

  console.log('All elements detected for textsize inputter');

  textSizeInputter.addEventListener('input', function() {
    if (this.value > 300) this.value = 300; // the maximum value is 300
    root.style.setProperty('--textsize', `${this.value}px`);
    console.log(`textsize changed to ${this.value}`);
  })
}

// main function
function main() {
  setupColorPicker();
  setupTextSizeInputter();
}

// run main() after all the DOM contents are loaded
document.addEventListener('DOMContentLoaded', function() {
  main();
})