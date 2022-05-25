const main_logic = () => {
  if (get_dom_list()[0]) {
    for (let i = 0; i < get_dom_list()[0].children.length; i++) {
      get_dom_list()[0].children[i].addEventListener("click", (e) => {
        e.preventDefault();
        for (let n = 0; n < get_dom_list()[1].children.length; n++) {
          if (
            get_dom_list()[1].children[n].classList.value.includes("selected")
          ) {
            get_dom_list()[1].children[n].click();
          }
        }

        if (get_dom_list()[2]) {
          for (let n = 0; n < get_dom_list()[2].children.length; n++) {
            if (get_dom_list()[2].children[n].classList.contains("selected")) {
              get_dom_list()[2].children[n].click();
            }
          }
        }
        const myTimeout = setTimeout(function () {
          if (get_dom_list()[1]) {
            const button_list = get_disabled_nodelist(
              get_dom_list()[1].children
            );
            if (button_list.length > 1) {
              for (let n = 0; n < get_dom_list()[1].children.length; n++) {
                if (
                  get_dom_list()[1].children[n].classList.value.includes(
                    "custom"
                  ) ||
                  get_dom_list()[1].children[n].getAttribute("data-value") ==
                    "custom"
                ) {
                  document
                    .querySelector('[data-name="Choose Diamond Carot"]')
                    .classList.add();
                  get_dom_list()[1].children[n].click();
                } else {
                  document.querySelector(
                    '[data-name="Choose Diamond Carot"]'
                  ).style.display = "flex";
                  document.querySelector(
                    '[data-name="Choose Diamond Carot"]'
                  ).style.visibility = "visible";
                }
              }
            }
          }
        }, 2);
      });
    }
  }
};
