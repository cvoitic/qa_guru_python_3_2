from selene.support.shared import browser
from selene import be, have

browser.config.hold_browser_open = True
browser.open('https://duckduckgo.com')
browser.element('[name="q"]').should(be.blank).type('selene yashaka').press_enter()
browser.element('[id="links"]').should(have.text('Selene - yashaka.github.io'))