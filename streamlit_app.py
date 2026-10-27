import streamlit as st
import altair as alt
import pandas as pd
from core import funnel, qualification
st.set_page_config(page_title='Adam Baig — GNO Senior SDR case study', page_icon='☎', layout='wide')
st.sidebar.markdown('### Adam Baig')
st.sidebar.caption('Senior SDR · GNO Partners case study')
p=st.sidebar.radio('Case study',['Start here','1 · Call playbook','2 · Objections','3 · Qualification & handoff','4 · Performance & coaching','5 · First 30 days'])
st.sidebar.link_button('My LinkedIn','https://www.linkedin.com/in/adambaiguk')
st.sidebar.link_button('Official vacancy','https://gno-partners.breezy.hr/p/66613b6bc3a3-sales-development-representative-b2b')
st.title('From first conversation to a qualified meeting')
st.markdown('<style>.block-container{max-width:1250px;padding-top:2.5rem}h1{letter-spacing:-0.035em}#MainMenu,.stAppDeployButton,[data-testid="stAppDeployButton"]{display:none}@media(max-width:600px){h1{font-size:2rem!important}h2{font-size:1.55rem!important}}</style>',unsafe_allow_html=True)
st.caption('GNO Partners Senior SDR case study · By Adam Baig')
if p=='Start here':
 st.header('Win the conversation. Earn the next step.')
 st.write('My approach: understand the owner’s commercial problem, establish a reason to meet, and give the Account Executive a useful handoff. Booked meetings only count when the right owners show up.')
 a,b,c=st.columns(3)
 a.markdown('**Primary work**  \nOutbound calls');b.markdown('**Lead source**  \nProvided lists');c.markdown('**Outcome**  \nQualified shows')
 st.info('Independent application exercise with fictional scenarios, illustrative metrics and proposed scripts.')
 st.subheader('The judgement I want to show')
 st.markdown('- Distinguish profitable growth from revenue growth.\n- Understand an existing agency before challenging it.\n- Qualify briefly without turning a cold call into discovery.\n- Act on coaching and measure attendance and AE acceptance.')
 st.subheader('Explore the case study')
 st.write('Try the call opener and objections, inspect the handoff, then adjust the funnel to see why meeting quality matters as much as activity.')
 with st.expander('Research notes · checked 27 October 2026'):
  st.markdown('[Official role](https://gno-partners.breezy.hr/p/66613b6bc3a3-sales-development-representative-b2b) · [Company website](https://gnopartners.com/)')
  st.write('The role specifies provided leads, predominantly outbound phone work, inbound follow-up, CRM accuracy, daily coaching and US Eastern overlap. GNO describes a consulting service with implementation support. Listed tools include Nooks, Instantly, Pipedrive, Slack and Gmail. Exact targets, qualification policy, pricing and compensation need confirmation.')
elif p.startswith('1'):
 st.header('A brief opener, then a useful question')
 st.markdown('''**Opener**  
“Hi Sam, Adam from GNO Partners — this is a cold call, can I have 20 seconds and you tell me if it’s worth continuing?”

**Reason to listen**  
“GNO has worked with over 1,300 Amazon brands. Our Done-With-You consulting model helps owners work on profitable growth. As you look at next quarter, is the bigger constraint acquiring sales profitably, keeping stock available, or something else?”

**Follow-up**  
“What has that changed in the business — margin, cash tied up in stock, or the time you spend fixing it?”

**Earn the meeting**  
“It sounds like [their stated problem] is worth a closer look. Let’s book a discovery conversation around that issue and see whether our approach fits. Is Thursday or Friday better for you?”''')
 st.table([{'Owner says':'Sales are up, cash is tight','Explore':'Stock cover, cash conversion and contribution; do not diagnose on a cold call.'},{'Owner says':'Ads cost too much','Explore':'Wasted spend, conversion or contribution after costs?'},{'Owner says':'Run everything for us','Explore':'Clarify the Done-With-You model: hands-on guidance and systems, with the owner’s team implementing.'}])
 st.write('Close with a clear next step: agree the meeting, confirm the timezone and restate the owner’s reason to attend.')
elif p.startswith('2'):
 st.header('Acknowledge → clarify → agree the next step')
 scripts={
 'We already have an agency':('That makes sense. Do they cover advertising alone, or the wider profit picture? If [stated gap] sits outside their remit, let’s explore that with the team. Can we pencil in a discovery call on Thursday with an agenda around that gap?','Anchor the meeting in an uncovered problem, rather than asking them to replace a provider.'),
 'Send information':('Happy to. Which issue should I focus on — margin, advertising efficiency or operations? If [stated issue] is a priority, a discovery conversation is the best way to explore it. Is Thursday or Friday better?','Offer useful information and return to a specific meeting ask.'),
 'No time':('Understood. When is a better two minutes — later today or first thing tomorrow?','Agree the exact callback time and timezone, then use that conversation to establish fit and ask for discovery.'),
 'We tried consultants':('I understand. What was missing last time — advice, implementation support or results? Our model is Done-With-You: hands-on guidance while your team builds the systems. Let’s explore whether that addresses [their concern]. Would an initial discovery conversation next week be useful?','Use the previous experience to focus discovery on what would need to be different.'),
 'What does it cost?':('The team can explain pricing alongside the support relevant to your business. Let’s book a discovery call to understand [stated problem] and discuss the commercial fit. Shall we set aside time on Thursday to cover both the problem and the commercial fit?','Surface cost early as part of the agenda; give pricing accurately once trained.'),
 'Run everything for us':('We are a Done-With-You consulting firm, rather than a Done-For-You agency. We help your team put the systems into practice. If that is the support you want, when could you and the person leading implementation join a discovery conversation?','Establish who will implement before passing the meeting to the AE.'),
 'Remove me':('Of course. I’ll record that you do not want further contact.','Stop outreach and record the request.')}
 choice=st.selectbox('Owner response',list(scripts));st.subheader('Suggested response');st.write(scripts[choice][0]);st.success(scripts[choice][1])
elif p.startswith('3'):
 st.header('Book the right next conversation')
 a,b=st.columns(2)
 with a:
  rev=st.selectbox('Illustrative annual revenue · USD',['Unknown','$1m–$9.9m','$10m–$99.9m','Below $1m'])
  checks=[st.checkbox(x) for x in ['Decision-maker access confirmed','Specific business pain stated','Owner agrees discovery purpose']]
  stop=st.checkbox('Owner requests no further contact')
  result=qualification(rev,checks,stop)
  if result=='stop': st.error('Stop outreach and record the preference.')
  elif result=='review': st.warning('Review fit with the AE: outside the illustrative target segment.')
  elif result=='clarify': st.warning('Clarify the missing information before booking.')
  else: st.success('Ready for AE review. Agree agenda, attendees and timezone; the AE confirms qualification.')
 with b:
  st.subheader('AE-ready handoff · brand A')
  st.markdown('''**Business:** Amazon homeware, owner-reported $4m sales.  
**Pain:** growing sales but contribution squeezed after ads and fulfilment.  
**Already tried:** advertising agency; operations internal.  
**Why now:** planning next quarter’s stock purchase.  
**Attendees:** owner; finance lead invited, unconfirmed.  
**Agenda:** understand margin constraints and whether consulting fits.  
**Unknowns:** actual contribution, budget and implementation capacity.  
**Next action:** confirm date, timezone and agreed agenda.''')
 with st.expander('Inbound enquiry: respond to the request, then establish fit'):
  st.write('Example enquiry: “We requested an analysis because advertising spend is rising faster than sales.”')
  st.write('Proposed response: “Hi Sam, Adam from GNO Partners, following up on your enquiry. Is now a good time? What prompted you to request the analysis?” Confirm the business, the owner’s issue and desired outcome before proposing discovery. Work to the agreed response-time target and record the enquiry source and next action.')
 st.subheader('A booking I would not call qualified')
 st.write('“Interested in growth; send an invite.” Revenue, authority and the reason to attend remain unknown. Clarify those points rather than pad the booking count.')
 with st.expander('Confirmation and no-show recovery'):
  st.write('Confirmation: “Thanks, Sam. We agreed to discuss margin after advertising and fulfilment on [date/time + timezone]. Does the invite work, and will your finance lead join?”')
  st.write('No-show: “Looks like today no longer worked. Is the margin discussion still a priority? Happy to find a better time; otherwise I will close the loop.”')
elif p.startswith('4'):
 st.header('Measure the path to qualified attendance')
 st.caption('Planning assumptions to calibrate with GNO’s daily KPIs. Expected counts are shown to one decimal place.')
 n=st.slider('Weekly dial attempts',100,3000,1000,50)
 st.caption('Default: 200 attempts per day across five days. Calibrate volume with the team, dialer setup and conversation quality.')
 labels=['Connect % of dials','Conversation % of connects','Booking % of conversations','Attendance % of bookings','Qualified % of attendees']
 cols=st.columns(5);rates=[cols[i].number_input(label,0,100,value=v) for i,(label,v) in enumerate(zip(labels,[12,65,25,80,75]))]
 values=funnel(n,rates)
 names=['Dials','Connections','Conversations','Bookings','Attended','Qualified attendees']
 frame=pd.DataFrame({'Stage':names,'Expected count':values})
 chart=alt.Chart(frame).mark_bar(color='#8b5cf6').encode(x=alt.X('Stage:N',sort=names,axis=alt.Axis(labelAngle=-25)),y=alt.Y('Expected count:Q'),tooltip=['Stage',alt.Tooltip('Expected count:Q',format='.1f')])
 st.altair_chart(chart,width='stretch')
 a,b,c=st.columns(3)
 a.metric('Expected bookings',f'{values[3]:.1f}')
 b.metric('Expected attendees',f'{values[4]:.1f}')
 c.metric('Qualified shows',f'{values[5]:.1f}')
 with st.expander('A coaching loop in practice'):
  st.write('Feedback: I explain too much before learning whether the owner has a problem. Next block: shorten the opener and ask one commercial question. Review: compare a coach-reviewed sample for meaningful conversations, not just a higher booking count. Keep the change if call quality improves; revise it with the coach if it does not.')
 st.subheader('Turn coaching into the next call block')
 st.table([{'Signal':'Bookings high; attendance low','Investigate':'Agenda, timing, commitment','Experiment':'Confirm the owner’s reason to attend and timezone.'},{'Signal':'Attendance high; AE acceptance low','Investigate':'Pain, authority, service fit','Experiment':'Review rejected meetings; add one focused question.'},{'Signal':'Connections but few conversations','Investigate':'Opener length and relevance','Experiment':'Review calls with the coach; test a shorter opener.'}])
 st.write('Proposed CRM flow: log commercial facts, objection, permission and next action in Pipedrive; use the team’s approved Nooks / Instantly setup. Follow up quickly on inbound enquiries.')
else:
 st.header('Learn the offer. Calibrate quality. Build repeatability.')
 st.table([{'Period':'Days 1–7','Focus':'Approved messaging, service fit, disqualification; listen to calls and shadow AEs.','Evidence':'Coach-reviewed role-play and agreed checklist.'},{'Period':'Days 8–14','Focus':'Coached call blocks, complete CRM notes, responsive inbound follow-up.','Evidence':'Call review and attendance baseline.'},{'Period':'Days 15–30','Focus':'Improve one bottleneck and close the AE feedback loop.','Evidence':'Weekly funnel review and documented experiment.'}])
 st.subheader('An operating rhythm I would calibrate with the team')
 st.write('Start with due callbacks, inbound enquiries and meeting confirmations. Protect focused outbound blocks around the agreed US Eastern overlap. Between blocks, complete CRM notes and review the next actions. Close the shift with one call-review takeaway and tomorrow’s follow-ups.')
 st.subheader('Questions for the hiring team')
 st.markdown('- What makes a meeting AE-accepted?\n- What are ramp activity, attendance and quality targets?\n- Which pricing and outcome claims may an SDR use?\n- What are approved follow-up and suppression processes?\n- What US Eastern overlap and coaching schedule are expected?')
 st.subheader('My case for the role')
 st.write('I bring 20+ years of phone-led recruitment and business development, including cold-calling directors and C-suite internationally. I have trained new consultants on the phone: earning attention, handling objections and asking for the next step.')
 st.markdown('- Filled approximately 75% of the recruitment roles I took on.\n- Built Ascent Energy Global from one person to 11 employees.\n- Helped grow Voyage Energy Group from 3 to 17 people.')
 st.write('For this role, I would bring that commercial drive to daily call blocks, qualified meetings and fast implementation of coaching. I am UK-based and can cover the required US Eastern working-hour overlap. Next step: put me through a live opener and objection-handling role-play.')
st.divider();st.caption('Adam Baig · GNO Senior SDR case study')
