const LANGUAGE_BTN = 'language-btn'
const langaugeBtns = document.querySelectorAll(`.${LANGUAGE_BTN}`)
const languageSwitch = document.querySelector('.language-switch')

langaugeBtns.forEach((btn) => {
  btn.addEventListener('click', () => {
    selectBtn(btn, langaugeBtns)
  })
})

languageSwitch.addEventListener('click', () => {
  const activeBtn = document.querySelector(`.${LANGUAGE_BTN}.active`)
  const nextLanguage = activeBtn.id === 'pt-br' ? 'en-us' : 'pt-br'
  const nextBtn = document.getElementById(nextLanguage)

  selectBtn(nextBtn, langaugeBtns)
})

function selectBtn(btn, allBtn) {
  allBtn.forEach((singleBtn) => {
    singleBtn.classList.remove('active')
  })

  btn.classList.add('active')
  btn.parentElement.dataset.language = btn.id
}
