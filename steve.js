const get_dom_list = ()=>{
	return document.querySelectorAll('.variable-items-wrapper')
}


const remove_disabled_class_from_btn = () => {
        setInterval(function () {
        if(get_dom_list()[0]){
                for (let j = 0; j < get_dom_list()[1].children.length; j++) {
                        if (get_dom_list()[1].children[j].classList.value.includes('custom')) {
                                get_dom_list()[1].children[j].style.display = 'none'
                                get_dom_list()[1].children[j].style.visibility = 'visible'
                        }
                }
                for (let i = 0; i < get_dom_list()[0].children.length; i++) {
                        get_dom_list()[0].children[i].classList.remove('disabled')
                }
        }
        }, 5);
}
remove_disabled_class_from_btn()
	
const get_disabled_nodelist = (node_list) => {
  let disabled_list = [];
  if(node_list){
  for (let i = 0; i < node_list.length; i++) {
    if (node_list[i].classList.value.includes("disabled")) {
      disabled_list.push(node_list[i]);
    }
  }
}
  return disabled_list;
};
	

const main_logic2 = () => {
  if(get_dom_list()[0]){
  for (let i = 0; i < get_dom_list()[0].children.length; i++) {
    get_dom_list()[0].children[i].addEventListener("click", (e) => {
      e.preventDefault();
      for (let n = 0; n < get_dom_list()[1].children.length; n++) {
        if ( get_dom_list()[1] && get_dom_list()[1].children[n].classList.value.includes("selected")) {
          get_dom_list()[1].children[n].click();
			
        }
      }
	}
    if(get_dom_list()[2]){
      for (let n = 0; n < get_dom_list()[2].children.length; n++) {
        if (et_dom_list()[2].children[n].classList.contains("selected")) {
           get_dom_list()[2].children[n].click();
        }
      }
 }
		
	
   const myTimeout = setTimeout(function () {
   const button_list = get_disabled_nodelist(get_dom_list()[1].children)
         if (button_list.length > 1) {
			if(get_dom_list()[1]){
			for (let n = 0; n < get_dom_list()[1].children.length; n++) {
				 if (get_dom_list()[1] && get_dom_list()[1].children[n].classList.value.includes('custom')) 
					    document.querySelector('[data-name="Choose Diamond Carot"]').style.display = 'none'
document.querySelector('[data-name="Choose Diamond Carot"]').style.visibility = 'hidden'
                        get_dom_list()[1].children[n].click()
					 
                }
		}else{
		document.querySelector('[data-name="Choose Diamond Carot"]').style.display = 'flex'
        document.querySelector('[data-name="Choose Diamond Carot"]').style.visibility = 'visible'
		}
		 }
}, 2);
    });
  }
};
	
main_logic2()
	
