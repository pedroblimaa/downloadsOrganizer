const LANGUAGE_BTN = 'language-btn'
const langaugeBtns = document.querySelectorAll(`.${LANGUAGE_BTN}`)

langaugeBtns.forEach((btn) => {
  btn.addEventListener('click', () => {
    selectBtn(btn, langaugeBtns)
  })
})

function selectBtn(btn, allBtn) {
  allBtn.forEach((singleBtn) => {
    singleBtn.classList.remove('active')
  })

  btn.classList.add('active')
}
