document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript loaded and running!');
    const playButton = document.getElementById('playButton');
    const moveButtonsContainer = document.getElementById('moveButtonsContainer');

    // Hide move buttons initially
    moveButtonsContainer.classList.add('hidden');

    playButton.addEventListener('click', () => {
        // Hide the play button
        playButton.classList.add('hidden');

        // Show the move buttons
        moveButtonsContainer.classList.remove('hidden');
    });
});