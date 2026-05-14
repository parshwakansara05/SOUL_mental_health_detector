import re

with open('templet/soul-analyzer.html', 'r', encoding='utf-8') as f:
    content = f.read()

replaces = [
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Gender</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Select your Gender</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Male</button>
              <button class="dropdown-option" role="option">Female</button>
              <button class="dropdown-option" role="option">Other</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Gender</label>
          <div class="dropdown-wrap" data-key="Gender">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Select your Gender</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Male</button>
              <button class="dropdown-option" role="option">Female</button>
            </div>
          </div>
        </div>'''
    ),
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Occupation</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Select your Occupation</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Student</button>
              <button class="dropdown-option" role="option">Employed</button>
              <button class="dropdown-option" role="option">Unemployed</button>
              <button class="dropdown-option" role="option">Retired</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Occupation</label>
          <div class="dropdown-wrap" data-key="Occupation">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Select your Occupation</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Student</button>
              <button class="dropdown-option" role="option">Corporate</button>
              <button class="dropdown-option" role="option">Business</button>
              <button class="dropdown-option" role="option">Housewife</button>
              <button class="dropdown-option" role="option">Others</button>
            </div>
          </div>
        </div>'''
    ),
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Self-Employed</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Are you self-employed ?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Self-Employed</label>
          <div class="dropdown-wrap" data-key="self_employed">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Are you self-employed ?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
            </div>
          </div>
        </div>'''
    ),
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Family_history</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Do you have a family history of mental health issues?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Family_history</label>
          <div class="dropdown-wrap" data-key="family_history">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Do you have a family history of mental health issues?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
            </div>
          </div>
        </div>'''
    ),
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Mental_Health_History</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Do you had any past mental health issues ?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Mental_Health_History</label>
          <div class="dropdown-wrap" data-key="Mental_Health_History">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Do you had any past mental health issues ?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
              <button class="dropdown-option" role="option">Maybe</button>
            </div>
          </div>
        </div>'''
    ),
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Days_Indoors</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">On average, how many days do you spend staying indoors ?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">1–14 days</button>
              <button class="dropdown-option" role="option">15–30 days</button>
              <button class="dropdown-option" role="option">31–60 days</button>
              <button class="dropdown-option" role="option">More than 2 months</button>
              <button class="dropdown-option" role="option">Go out every day</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Days_Indoors</label>
          <div class="dropdown-wrap" data-key="Days_Indoors">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">On average, how many days do you spend staying indoors ?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">1-14 days</button>
              <button class="dropdown-option" role="option">15-30 days</button>
              <button class="dropdown-option" role="option">31-60 days</button>
              <button class="dropdown-option" role="option">More than 2 months</button>
              <button class="dropdown-option" role="option">Go out Every day</button>
            </div>
          </div>
        </div>'''
    ),
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Growing_Stress</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Select your current stress level</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Low</button>
              <button class="dropdown-option" role="option">Medium</button>
              <button class="dropdown-option" role="option">High</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Growing_Stress</label>
          <div class="dropdown-wrap" data-key="Growing_Stress">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Select your current stress level</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
              <button class="dropdown-option" role="option">Maybe</button>
            </div>
          </div>
        </div>'''
    ),
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Mood_Swings</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Do you experience frequent mood swings?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Mood_Swings</label>
          <div class="dropdown-wrap" data-key="Mood_Swings">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Do you experience frequent mood swings?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">High</button>
              <button class="dropdown-option" role="option">Medium</button>
              <button class="dropdown-option" role="option">Low</button>
            </div>
          </div>
        </div>'''
    ),
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Changes_Habits</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Have you noticed changes in your daily habits recently?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Changes_Habits</label>
          <div class="dropdown-wrap" data-key="Changes_Habits">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Have you noticed changes in your daily habits recently?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
              <button class="dropdown-option" role="option">Maybe</button>
            </div>
          </div>
        </div>'''
    ),
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Coping_Struggles</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Are you finding it difficult to cope with daily challenges?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Coping_Struggles</label>
          <div class="dropdown-wrap" data-key="Coping_Struggles">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Are you finding it difficult to cope with daily challenges?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
            </div>
          </div>
        </div>'''
    ),
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Work/Studies_Interest</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Select your level of interest in work or studies</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Low</button>
              <button class="dropdown-option" role="option">Medium</button>
              <button class="dropdown-option" role="option">High</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Work/Studies_Interest</label>
          <div class="dropdown-wrap" data-key="Work_Interest">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Select your level of interest in work or studies</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
              <button class="dropdown-option" role="option">Maybe</button>
            </div>
          </div>
        </div>'''
    ),
    (
        '''<div class="input-col">
          <label><span class="req">*</span>Social_Weakness</label>
          <div class="dropdown-wrap">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Do you feel uncomfortable in social situations?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
            </div>
          </div>
        </div>''',
        '''<div class="input-col">
          <label><span class="req">*</span>Social_Weakness</label>
          <div class="dropdown-wrap" data-key="Social_Weakness">
            <div class="dropdown-trigger" tabindex="0" role="button" aria-haspopup="listbox">
              <span class="trigger-text">Do you feel uncomfortable in social situations?</span>
              <span class="chevron-wrap"><img src="https://www.figma.com/api/mcp/asset/2eb7c1d9-9a88-4b9c-9889-aac618d20fd7" alt="" /></span>
            </div>
            <div class="dropdown-options" role="listbox">
              <button class="dropdown-option" role="option">Yes</button>
              <button class="dropdown-option" role="option">No</button>
              <button class="dropdown-option" role="option">Maybe</button>
            </div>
          </div>
        </div>'''
    )
]

for orig, new in replaces:
    if orig not in content:
        print("FAILED TO FIND:", orig[:50])
    content = content.replace(orig, new)

with open('templet/soul-analyzer.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated soul-analyzer.html")
