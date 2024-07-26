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
            document.querySelector('button').disabled = true;
            setTimeout(() => {
                document.querySelector('button').disabled = false;
                messageElement.textContent = '';
                guessesLeftElement.textContent = 'You have 3 guesses left.';
                document.getElementById('guess-input').value = '';
            }, 3000);
        }
    });
}