# Adam Baig — GNO Senior SDR case study

[Open the interactive case study](https://adam-baig-sdr-case-study.streamlit.app/)

A practical application exercise focused on turning owner conversations into qualified discovery meetings. Built for the GNO Partners Senior SDR role.

- Call opener and commercially focused follow-up questions.
- Seven objection examples with varied closes and a clear opt-out response.
- Qualification, inbound enquiry, AE handoff and no-show follow-up examples.
- Adjustable performance funnel, coaching loop and first-30-days plan.

Independent exercise: scenarios, metrics and scripts are illustrative.

## Run locally
Use Python 3.12 or later, install the dependencies and start the app:

    python -m pip install -r requirements.txt
    python -m streamlit run streamlit_app.py

## Validation

    python -m pytest -q

13 tests cover funnel denominators, boundary values, qualification and opt-out precedence. All six sections and seven objection states also rendered without exceptions in local Streamlit AppTest checks.

## Sources and contact
[Official vacancy](https://gno-partners.breezy.hr/p/66613b6bc3a3-sales-development-representative-b2b) · [GNO Partners](https://gnopartners.com/) · [Adam Baig on LinkedIn](https://www.linkedin.com/in/adambaiguk)

The app does not connect to a CRM, dialer or language-model service. No outreach is sent.
