const add_disable_to_btn = (btn) => {
        btn.classList.add('disabled')
        btn.setAttribute('aria-checked', 'false')
}
const remove_disable_from_btn = (btn) => {
        btn.classList.remove('disabled')
        btn.setAttribute('aria-checked', 'false')
}

const hide = (node) => {
        node.style.display = 'none !important'
        node.style.visibility = 'visible !important'
}
const show = (node) => {
        node.style.display = 'flex !important'
        node.style.visibility = 'visible !important'
}

const get_element_with_class_none = (node_list) => {
  for (let i = 0; i < node_list.length; i++) {
    if (node_list[i].classList.value.includes("custom")) {
      return node_list[i];
    }
  }
};

const get_disabled_nodelist = (node_list) => {
  let disabled_list = [];
  for (let i = 0; i < node_list.length; i++) {
    if (node_list[i].classList.value.includes("disabled")) {
      disabled_list.push(node_list[i]);
    }
  }
  return disabled_list;
};

// const remove_disabled_class_from_btn = () => {
//   setInterval(function () {
//     for (let j = 0; j < get_dom_list()[1].children.length; j++) {
//       if (get_dom_list()[1].children[j].classList.value.includes("custom")) {
//         //                                 get_dom_list()[1].children[j].style.display = 'none'
//         //                                 get_dom_list()[1].children[j].style.visibility = 'visible'
//       }
//     }
//     for (let i = 0; i < get_dom_list()[0].children.length; i++) {
//       get_dom_list()[0].children[i].classList.remove("disabled");
//     }
//   }, 10);
// };

// remove_disabled_class_from_btn();

// const nodes1 = get_dom_list()[0].childNodes;
// const nodes2 = get_dom_list()[1].children;
// const nodes3 = get_dom_list()[2].childNodes;
// nodes1.forEach((node) => {
//   node.addEventListener("click", (e) => {
//     document.querySelector('[title="Custom"]');
//     if (get_disabled_nodelist(nodes2).length > 1) {
//       document.querySelector('[title="Custom"]').click();
//     } else {
//       document.querySelector('[title="Custom"]').click();
//     }
//   });
// });

const get_element_with_class_selected = (node_list) => {
        for (let i = 0; i < node_list.length; i++) {
                if (node_list[i].classList.value.contains('selected')) {
                        element_with_selected = node_list[i]
                }

        }
}

const remove_disabled_class_from_btn = () => {
        setInterval(function () {
                for (let j = 0; j < get_dom_list()[1].children.length; j++) {
                        if (get_dom_list()[1].children[j].classList.value.includes('custom')) {
                                get_dom_list()[1].children[j].style.display = 'none'
//                                 get_dom_list()[1].children[j].style.visibility = 'visible'
                        }
                }
                for (let i = 0; i < get_dom_list()[0].children.length; i++) {
                        get_dom_list()[0].children[i].classList.remove('disabled')
                }
        }, 10);
}

const remove_selected_class_from_default_btn = () => {
        for (let i = 0; i < get_dom_list()[1].children.length; i++) {
                if (get_dom_list()[1].children[i].classList.value.includes('custom')) {
                        get_dom_list()[1].children[i].classList.add('disabled')
                        get_dom_list()[1].children[i].classList.remove('selected')
                        get_dom_list()[1].children[i].setAttribute('aria-checked', 'false')
                }
        }
}

const get_selected_nodelist = (node_list) => {
        let disabled_list = []
        for (let i = 0; i < node_list.length; i++) {
                if (node_list[i].classList.value.includes('selected')) {
                        disabled_list.push(node_list[i])
                }

        }
        return disabled_list
}

const remove_selection_from_btn = (node) =>{
	node.classList.remove('selected')
	node.setAttribute('aria-checked', 'false')

}

const remove_element_with_none = () => {
        for (let i = 0; i < get_dom_list()[1].children.length; i++) {
                let singleitem = get_element_with_class_none(get_dom_list()[1].children)
                let disabled_button_list = get_disabled_nodelist(get_dom_list()[0].children)
                if (singleitem) {
                        if (disabled_button_list.length > 1) {
                                add_selection_to_btn(get_dom_list()[1].children[i])
//                                 hide(get_dom_list()[1].children[i])
                        } else if (disabled_button_list.length < 1) {
                                remove_selection_from_btn(get_dom_list()[1].children[i])
                                remove_selection_from_btn(get_dom_list()[1].children[i])
                        }
                }
        }
}

for (let index = 0; index < get_dom_list()[1].children.length; index++) {
        get_dom_list()[1].children[index].addEventListener('click', () => {
                for (let i = 0; i < get_dom_list()[1].children.length; i++) {
                        if (get_dom_list()[1].children[i].classList.contains('button_active')) {
                                get_dom_list()[1].children[i].classList.remove('button_active')
                        }
                }
                get_dom_list()[1].children[index].classList.add('button_active')
        })

}

for (let i = 0; i < get_dom_list()[0].children.length; i++) {
        get_dom_list()[0].children[i].addEventListener('click', (e) => {
                e.preventDefault()
                const button_list = get_disabled_nodelist(get_dom_list()[1].children)
                if (!button_list.length > 1) {

                        document.querySelectorAll('h4')[1].classList.remove('show')
                        document.querySelectorAll('h4')[1].classList.add('hide')
                        hide(get_dom_list()[1])
                } else {
                        document.querySelectorAll('h4')[1].classList.remove('hide')
                        document.querySelectorAll('h4')[1].classList.add('show')
                        show(get_dom_list()[1])

                }
        })
}

const main_logic = () => {
        for (let i = 0; i < get_dom_list()[0].children.length; i++) {
                get_dom_list()[0].children[i].addEventListener('click', (e) => {
                        e.preventDefault()
                        for (let index = 0; index < get_dom_list()[0].children.length; index++) {
                                if (get_dom_list()[0].children[index].classList.contains('button_active')) {
                                        get_dom_list()[0].children[index].classList.remove('button_active')
                                        get_dom_list()[0].children[index].classList.remove('selected')
                                }

                        }
                        get_dom_list()[0].children[i].classList.add('button_active')

                        if (get_disabled_nodelist(get_dom_list()[1].children).length > 1) {
                                if (get_dom_list()[1].children[i].classList.value.includes('custom')) {
                                        get_dom_list()[1].children[i].classList.contains('selected')
                                        get_dom_list()[1].classList.remove('show')
                                        get_dom_list()[1].classList.add('hide')
                                }

                        } else if (get_selected_nodelist(get_dom_list()[1].children).length > 1) {
                                for (let i = 0; i < get_dom_list()[1].children.length; i++) {
                                        if (get_dom_list()[1].children[i].classList.value.includes('custom')) {
                                                get_dom_list()[1].children[i].classList.add('disabled')
                                                get_dom_list()[1].children[i].classList.remove('selected')
                                                get_dom_list()[1].children[i].setAttribute('aria-checked', 'false')
                                        }
                                }

                                get_dom_list()[1].classList.remove('hide')
                                get_dom_list()[1].classList.add('show')

                        } else {
                                get_dom_list()[1].classList.add('show')
                        }
                        var selected = []
                        for (let n = 0; n < get_dom_list()[0].children.length; n++) {
                                if (get_dom_list()[0].children[n].classList.contains('selected')) {
                                        selected.push(get_dom_list()[0].children[n])
                                }
                        }
                        if (selected.length < 1) {
                                setTimeout(() => {
                                        for (let i = 0; i < get_dom_list()[1].children.length; i++) {
                                                if (get_dom_list()[1].children[i].classList.value.includes('custom')) {
                                                        get_dom_list()[1].children[i].classList.remove('disabled')
                                                        get_dom_list()[1].children[i].classList.add('selected')
                                                        get_dom_list()[1].children[i].setAttribute('aria-checked', 'true')
                                                        if (get_disabled_nodelist(get_dom_list()[1].children).length > 1) {
                                                                document.querySelector('.single_add_to_cart_button').classList.remove('disabled')
                                                        }

                                                }
                                        }
                                }, 10)

                        } else {
                                setTimeout(() => {

                                        for (let i = 0; i < get_dom_list()[1].children.length; i++) {
                                                if (get_dom_list()[1].children[i].classList.value.includes('custom')) {
                                                        get_dom_list()[1].children[i].classList.add('disabled')
                                                        get_dom_list()[1].children[i].classList.remove('selected')
                                                        get_dom_list()[1].classList.remove('disabled')
                                                        get_dom_list()[1].children[i].setAttribute('aria-checked', 'false')
                                                }
                                        }

                                }, 10)

                        }

                })

        }

}

remove_element_with_none()
remove_disabled_class_from_btn()
remove_selected_class_from_default_btn()
main_logic()
