const copyBtns = [...document.getElementsByClassName('copy-btn')]
 

let previous = null

copyBtns.forEach(btn=> btn.addEventListener('click',()=>{
 
  const gallery =btn.getAttribute('data-gallery')
 
  navigator.clipboard.writeText(gallery)
  btn.textContent = ('copied')

  navigator.clipboard.readText().then(clipText =>{
    console.log(clipText)
    btn.textContent = `copied ${clipText}`
  })

  if (previous){
   previous.textContent = "click"
  }
  previous = btn
}))