document.addEventListener('DOMContentLoaded', async () => {
  try {
    const apiUrl =
      'https://walrus-app-jbfmz.ondigitalocean.app/vegetable_infos';
    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    const main = document.getElementById('container_allVegetables');
    const families = [...new Set(data.map((item) => item.family))].sort();

    for (const familyName of families) {
      const subtitle = createSubtitleElement(familyName);
      const container = createContainerElement();

      main.appendChild(subtitle);
      main.appendChild(container);

      const sortedVegetables = data
        .filter((vegetable) => vegetable.family === familyName)
        .sort((a, b) => a.name.localeCompare(b.name));

      sortedVegetables.forEach((vegetable) => {
        const item = createItemElement(vegetable);
        container.appendChild(item);
      });
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});

function createSubtitleElement(text) {
  const subtitle = document.createElement('div');
  subtitle.className = 'allVegetables__subtitle';
  subtitle.textContent = text;
  return subtitle;
}

function createContainerElement() {
  const container = document.createElement('div');
  container.className = 'allVegetables__container';
  return container;
}

function createItemElement(vegetable) {
  const item = document.createElement('div');
  item.className = 'allVegetables__item';
  const vegetable_name = vegetable.name;
  const vegetable_name_without_spaces = vegetable_name.replace(/\s/g, '');
  const imgUrl = `url(./styles/assets/vegetable_icons/${vegetable_name_without_spaces}.png)`;
  item.style.backgroundImage = imgUrl;

  const nameSpan = document.createElement('span');
  nameSpan.textContent = vegetable.name;
  item.appendChild(nameSpan);

  return item;
}
