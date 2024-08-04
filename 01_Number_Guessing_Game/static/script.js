let randomNumber;
let guessesLeft;

function startGame() {
    randomNumber = Math.floor(Math.random() * 10) + 1;
    guessesLeft = 3;
    const guessInput = document.getElementById('guess-input');
    document.getElementById('play-button').style.display = 'none';
    document.getElementById('game-elements').style.display = 'block';
    document.getElementById('message').textContent = '';
    document.getElementById('guesses-left').textContent = 'You have 3 guesses left.';
    guessInput.value = '';
    guessInput.classList.remove('input-correct', 'input-incorrect');
}

function makeGuess() {
    const userGuess = parseInt(document.getElementById('guess-input').value);
    const messageElement = document.getElementById('message');
    const guessesLeftElement = document.getElementById('guesses-left');
    const guessInput = document.getElementById('guess-input');

    fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            guess: userGuess
        })
    })
    .then(response => response.json())
    .then(data => {
        messageElement.textContent = data.message;
        messageElement.style.display = 'block';
        guessesLeftElement.textContent = `You have ${data.guesses_left} guesses left.`;

        if (data.correct) {
            guessInput.classList.remove('input-incorrect');
            guessInput.classList.add('input-correct');
        } else {
            guessInput.classList.remove('input-correct');
            guessInput.classList.add('input-incorrect');
        }

        setTimeout(() => {
            guessInput.classList.remove('input-incorrect');
        }, 700);

        if (data.correct || data.guesses_left === 0) {
            document.getElementById('guess-button').disabled = true;
            setTimeout(() => {
                document.getElementById('guess-button').disabled = false;
                messageElement.style.display = 'none';
                guessInput.value = '';
                document.getElementById('play-button').style.display = 'flex';
                document.getElementById('game-elements').style.display = 'none';
            }, 1800);
        }
    });
}

document.addEventListener('keydown', function (event) {
    if (event.key === 'Enter' && document.getElementById('game-elements').style.display === 'block') {
        event.preventDefault();
        if (!event.repeat) {
            makeGuess();
        }
    }
});