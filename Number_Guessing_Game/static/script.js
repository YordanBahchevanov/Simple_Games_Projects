let randomNumber;
let guessesLeft;

function startGame() {
    randomNumber = Math.floor(Math.random() * 10) + 1;
    guessesLeft = 3;
    document.getElementById('play-button').style.display = 'none';
    document.getElementById('game-elements').style.display = 'block';
    document.getElementById('message').textContent = '';
    document.getElementById('guesses-left').textContent = 'You have 3 guesses left.';
    document.getElementById('guess-input').value = '';
}

function makeGuess() {
    const userGuess = parseInt(document.getElementById('guess-input').value);
    const messageElement = document.getElementById('message');
    const guessesLeftElement = document.getElementById('guesses-left');

    fetch( '/guess', {
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
        guessesLeftElement.textContent = `You have ${data.guesses_left} guesses left.`;

        if (data.correct || data.guesses_left === 0) {
            document.querySelector('button[onclick="makeGuess()"]').disabled = true;
            setTimeout(() => {
                document.querySelector('button[onclick="makeGuess()"]').disabled = false;
                messageElement.textContent = '';
                guessesLeftElement.textContent = 'You have 3 guesses left.';
                document.getElementById('guess-input').value = '';
                document.getElementById('play-button').style.display = 'flex';
                document.getElementById('game-elements').style.display = 'none';
            }, 2000);
        }
    });
}