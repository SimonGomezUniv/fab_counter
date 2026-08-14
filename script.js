const STARTING_LIFE = 20;
const lifeValues = [STARTING_LIFE, STARTING_LIFE];

const nameInputs = Array.from(document.querySelectorAll('.player-name-input'));

const lifeElements = Array.from({ length: 2 }, (_, index) => {
  const el = document.getElementById(`life-${index}`);
  if (!el) {
    throw new Error(`Missing counter element for player ${index}`);
  }
  return el;
});

function updateLifeDisplay(playerIndex) {
  lifeElements[playerIndex].textContent = String(lifeValues[playerIndex]);
}

function syncPlayerName(playerIndex) {
  const input = nameInputs[playerIndex];
  if (!input) return;

  const value = input.value.trim();
  input.value = value || `Joueur ${playerIndex + 1}`;
  input.setAttribute('aria-label', `Nom du joueur ${playerIndex + 1}`);
}

function adjustLife(playerIndex, delta) {
  const nextValue = Math.max(0, lifeValues[playerIndex] + delta);
  lifeValues[playerIndex] = nextValue;
  updateLifeDisplay(playerIndex);
}

function resetLife(playerIndex) {
  lifeValues[playerIndex] = STARTING_LIFE;
  updateLifeDisplay(playerIndex);
}

document.querySelectorAll('.zone-button').forEach((button) => {
  button.addEventListener('click', () => {
    const playerIndex = Number(button.dataset.player);
    const delta = Number(button.dataset.change);
    adjustLife(playerIndex, delta);
  });
});

document.querySelectorAll('.reset-button').forEach((button) => {
  button.addEventListener('click', () => {
    const playerIndex = Number(button.dataset.reset);
    resetLife(playerIndex);
  });
});

nameInputs.forEach((input, index) => {
  input.addEventListener('input', () => {
    syncPlayerName(index);
  });

  input.addEventListener('blur', () => {
    syncPlayerName(index);
  });
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'ArrowLeft' || event.key.toLowerCase() === 'a') {
    adjustLife(0, -1);
  }

  if (event.key === 'ArrowRight' || event.key.toLowerCase() === 'd') {
    adjustLife(0, 1);
  }

  if (event.key === 'ArrowDown' || event.key.toLowerCase() === 's') {
    adjustLife(1, -1);
  }

  if (event.key === 'ArrowUp' || event.key.toLowerCase() === 'w') {
    adjustLife(1, 1);
  }

  if (event.key.toLowerCase() === 'r') {
    resetLife(0);
    resetLife(1);
  }
});

lifeValues.forEach((_, index) => updateLifeDisplay(index));
