var mode = 'dark';
const root = document.querySelector(':root');

// setup the mode change buttons (light and dark)
function setupModeButtons() {
  const lightModeButton = document.querySelector('.light-mode-border');
  const darkModeButton = document.querySelector('.dark-mode-border');
  const appTitle= document.querySelector('.app-title-text');
  if (!lightModeButton || !darkModeButton || !appTitle) return;

  console.log('All elements detected for mode button');

  lightModeButton.addEventListener('click', function() {
    if (mode !== 'light') {
      root.style.setProperty('--primarycolor', '#2c2c2c');
      root.style.setProperty('--textcolor', '#2c2c2c');
      root.style.setProperty('--bordercolor', '#c0c0c0');
      root.style.setProperty('--background1', '#cacaca');
      root.style.setProperty('--background2', '#d9d9d9');
      appTitle.style.setProperty('color', '#5c5c5c');
      lightModeButton.style.setProperty('background', 'linear-gradient(-45deg, #00b2ff, #f36eff)');
      darkModeButton.style.setProperty('background', '#343434');
      mode = 'light';
      console.log("light-mode button clicked");
    }
  });

  darkModeButton.addEventListener('click', function() {
    if (mode !== 'dark') {
      root.style.setProperty('--primarycolor', '#eeeeee');
      root.style.setProperty('--textcolor', '#eeeeee');
      root.style.setProperty('--bordercolor', '#515151');
      root.style.setProperty('--background1', '#2b2b2b');
      root.style.setProperty('--background2', '#343434');
      appTitle.style.setProperty('color', '#cbcbcb');
      lightModeButton.style.setProperty('background', '#d9d9d9');
      darkModeButton.style.setProperty('background', 'linear-gradient(-45deg, #00b2ff, #f36eff)');
      mode = 'dark';
      console.log("dark-mode button clicked");
    }
  });
}

// setup the color picker function
// when the user inputs a color, reflect it to --textcolor variable in styles.css
function setupColorPicker() {
  const colorPicker = document.querySelector('.textcolor-picker');
  if (!colorPicker) return;

  console.log('All elements detected for color picker');

  colorPicker.addEventListener('input', function() {
    root.style.setProperty('--textcolor', this.value);
    console.log(`colour changed to ${this.value}`);
  });
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
  });
}

function setupResponseButton() {
  const responseButton = document.querySelector('.response-button');
  const editor = document.querySelector('.editor');
  console.log("setupResponseButton() called");

  if (!responseButton || !editor) return;

  responseButton.addEventListener('click', function() {
    const text = editor.value; // text value to send to the function
    console.log(`text is: ${text}`);

    fetch('/get_response/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCsrfToken()
      },
      body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
      editor.value += '\n' + data.result;
      console.log("Added text");
    })
    .catch((error) => {
      console.error('Error:', error)
    });
  });
}

function getCsrfToken() {
  const cookies = document.cookie.split(';');
  for (const cookie of cookies) {
      const [name, value] = cookie.split('=');
      if (name.trim() === 'csrftoken') {
          return value;
      }
  }
  return '';
}

// main function
function main() {
  console.log("main program ran");
  setupModeButtons();
  setupColorPicker();
  setupTextSizeInputter();
  setupResponseButton();
}

// run main() after all the DOM contents are loaded
document.addEventListener('DOMContentLoaded', function() {
  main();
});