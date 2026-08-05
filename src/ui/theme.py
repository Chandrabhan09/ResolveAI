import streamlit as st


def apply_resolve_theme():
    """
    Global ResolveAI premium monochrome UI theme.
    """

    st.markdown(
        """
        <style>

        /* =========================================
           GLOBAL
        ========================================= */

        .stApp {
            background:
                radial-gradient(
                    circle at 50% 15%,
                    rgba(255, 255, 255, 0.055),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 85% 55%,
                    rgba(255, 255, 255, 0.025),
                    transparent 25%
                ),
                #050505;

            color: #f5f5f5;
        }


        html,
        body,
        [class*="css"] {
            font-family:
                Inter,
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif;
        }


        /* =========================================
           MAIN CONTENT
        ========================================= */

        .block-container {
            max-width: 1500px;

            padding-top: 2rem;
            padding-left: 3rem;
            padding-right: 3rem;
            padding-bottom: 4rem;
        }


        /* =========================================
           TEXT
        ========================================= */

        h1,
        h2,
        h3 {
            color: #f7f7f7 !important;
            letter-spacing: -0.025em;
        }


        p,
        span,
        label {
            color: #b5b5b5;
        }


        /* =========================================
           SCROLLBAR
        ========================================= */

        ::-webkit-scrollbar {
            width: 6px;
        }

        ::-webkit-scrollbar-track {
            background: #080808;
        }

        ::-webkit-scrollbar-thumb {
            background: #343434;
            border-radius: 20px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #505050;
        }


        /* =========================================
           BUTTONS
        ========================================= */

        .stButton > button {

            width: 100%;

            min-height: 44px;

            border-radius: 12px;

            border: 1px solid rgba(255,255,255,0.12);

            background:
                linear-gradient(
                    180deg,
                    rgba(255,255,255,0.07),
                    rgba(255,255,255,0.025)
                );

            color: #eeeeee;

            font-weight: 500;

            transition:
                border-color 0.2s ease,
                background 0.2s ease,
                transform 0.2s ease;
        }


        .stButton > button:hover {

            border-color: rgba(255,255,255,0.28);

            background:
                linear-gradient(
                    180deg,
                    rgba(255,255,255,0.11),
                    rgba(255,255,255,0.045)
                );

            transform: translateY(-1px);

            color: #ffffff;
        }


        .stButton > button:active {
            transform: translateY(0);
        }


        /* =========================================
           TEXT INPUT
        ========================================= */

        .stTextInput input {

            background: rgba(255,255,255,0.045) !important;

            color: #f5f5f5 !important;

            border:
                1px solid rgba(255,255,255,0.12) !important;

            border-radius: 12px !important;

            min-height: 46px;

            transition:
                border-color 0.2s ease,
                box-shadow 0.2s ease;
        }


        .stTextInput input:focus {

            border-color:
                rgba(255,255,255,0.30) !important;

            box-shadow:
                0 0 0 1px rgba(255,255,255,0.08),
                0 0 25px rgba(255,255,255,0.035) !important;
        }


        /* =========================================
           CHAT INPUT
        ========================================= */

        [data-testid="stChatInput"] {

            background:
                rgba(22,22,22,0.86);

            border:
                1px solid rgba(255,255,255,0.16);

            border-radius: 18px;

            box-shadow:
                0 18px 60px rgba(0,0,0,0.55),
                inset 0 1px 0 rgba(255,255,255,0.04);

            backdrop-filter: blur(20px);

            overflow: hidden;
        }


        [data-testid="stChatInput"] textarea {

            color: #f4f4f4 !important;

            background: transparent !important;
        }


        [data-testid="stChatInput"] textarea::placeholder {
            color: #737373 !important;
        }


        /* =========================================
           CHAT MESSAGES
        ========================================= */

        [data-testid="stChatMessage"] {

            background:
                rgba(255,255,255,0.025);

            border:
                1px solid rgba(255,255,255,0.07);

            border-radius: 16px;

            padding: 1rem;

            margin-bottom: 0.8rem;
        }


        /* =========================================
           METRICS
        ========================================= */

        [data-testid="stMetric"] {

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.055),
                    rgba(255,255,255,0.018)
                );

            border:
                1px solid rgba(255,255,255,0.09);

            border-radius: 16px;

            padding: 18px;

            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.025);
        }


        [data-testid="stMetricValue"] {
            color: #ffffff;
        }


        /* =========================================
           SELECT BOX
        ========================================= */

        [data-baseweb="select"] > div {

            background:
                rgba(255,255,255,0.045) !important;

            border-color:
                rgba(255,255,255,0.12) !important;

            border-radius: 12px !important;
        }


        /* =========================================
           ALERTS
        ========================================= */

        [data-testid="stAlert"] {

            background:
                rgba(255,255,255,0.035);

            border:
                1px solid rgba(255,255,255,0.08);

            border-radius: 14px;

            color: #d5d5d5;
        }


        /* =========================================
           DIVIDERS
        ========================================= */

        hr {

            border: none !important;

            height: 1px !important;

            background:
                rgba(255,255,255,0.08) !important;

            margin:
                1.5rem 0 !important;
        }


        /* =========================================
           SIDEBAR
        ========================================= */

        [data-testid="stSidebar"] {

            background:
                linear-gradient(
                    180deg,
                    #0b0b0b,
                    #070707
                );

            border-right:
                1px solid rgba(255,255,255,0.08);
        }


        [data-testid="stSidebar"] > div:first-child {

            background: transparent;
        }


        /* =========================================
           PREMIUM GLASS CARD
        ========================================= */

        .resolve-glass-card {

            padding: 22px;

            border-radius: 18px;

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.055),
                    rgba(255,255,255,0.018)
                );

            border:
                1px solid rgba(255,255,255,0.10);

            box-shadow:
                0 20px 60px rgba(0,0,0,0.28),
                inset 0 1px 0 rgba(255,255,255,0.035);

            backdrop-filter: blur(18px);
        }


        /* =========================================
           HERO
        ========================================= */

        .resolve-hero {

            text-align: center;

            padding:
                3.5rem 1rem 2rem 1rem;
        }


        .resolve-orb {

            width: 76px;
            height: 76px;

            margin:
                0 auto 24px auto;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 24px;

            color: #ffffff;

            font-size: 30px;

            font-weight: 600;

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.13),
                    rgba(255,255,255,0.025)
                );

            border:
                1px solid rgba(255,255,255,0.16);

            box-shadow:
                0 0 30px rgba(255,255,255,0.08),
                0 0 80px rgba(255,255,255,0.045),
                inset 0 1px 0 rgba(255,255,255,0.12);
        }


        .resolve-hero-title {

            color: #f7f7f7;

            font-size: clamp(
                2rem,
                4vw,
                3.6rem
            );

            font-weight: 500;

            line-height: 1.08;

            letter-spacing: -0.045em;

            margin-bottom: 14px;
        }


        .resolve-hero-subtitle {

            max-width: 620px;

            margin: auto;

            color: #7f7f7f;

            font-size: 1rem;

            line-height: 1.65;
        }


        /* =========================================
           SMALL LABEL
        ========================================= */

        .resolve-label {

            color: #707070;

            font-size: 0.72rem;

            font-weight: 600;

            letter-spacing: 0.09em;

            text-transform: uppercase;

            margin-bottom: 10px;
        }


        /* =========================================
           MOBILE
        ========================================= */

        @media (max-width: 768px) {

            .block-container {

                padding-left: 1rem;

                padding-right: 1rem;

                padding-top: 1rem;
            }


            .resolve-hero {

                padding-top: 2rem;
            }


            .resolve-hero-title {

                font-size: 2.1rem;
            }


            .resolve-orb {

                width: 64px;
                height: 64px;

                border-radius: 20px;
            }
        }
        
        /* =========================================================
        STEP 7.3.5 — CINEMATIC AI SUPPORT POLISH
        ========================================================= */


        /* ---------- Main cinematic workspace ---------- */

        [data-testid="stMain"] {
            background:
                radial-gradient(
                    ellipse at 52% 25%,
                    rgba(255,255,255,0.075) 0%,
                    rgba(255,255,255,0.025) 22%,
                    transparent 48%
                ),
                radial-gradient(
                    ellipse at 70% 65%,
                    rgba(255,255,255,0.025),
                    transparent 40%
                ),
                #050505;
        }


        /* ---------- Hide unnecessary Streamlit chrome ---------- */

        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        [data-testid="stStatusWidget"] {
            visibility: hidden;
        }


        /* ---------- Main container ---------- */

        .block-container {
            max-width: 1440px !important;

            padding-top: 1.4rem !important;
            padding-bottom: 3rem !important;

            padding-left: 2.5rem !important;
            padding-right: 2.5rem !important;
        }


        /* =========================================================
        HERO
        ========================================================= */

        .resolve-hero {
            position: relative;

            text-align: center;

            max-width: 850px;

            margin:
                2.5rem auto 1.8rem auto;

            padding:
                3.5rem 1rem 2rem 1rem;
        }


        /* central vertical glow */

        .resolve-hero::before {
            content: "";

            position: absolute;

            width: 280px;
            height: 300px;

            left: 50%;
            top: -55px;

            transform:
                translateX(-50%);

            background:
                radial-gradient(
                    ellipse,
                    rgba(255,255,255,0.15) 0%,
                    rgba(255,255,255,0.055) 30%,
                    transparent 70%
                );

            filter: blur(24px);

            pointer-events: none;

            z-index: 0;
        }


        /* vertical light beam */

        .resolve-hero::after {
            content: "";

            position: absolute;

            width: 2px;
            height: 170px;

            left: 50%;
            top: -70px;

            transform:
                translateX(-50%);

            background:
                linear-gradient(
                    to bottom,
                    transparent,
                    rgba(255,255,255,0.30),
                    rgba(255,255,255,0.04),
                    transparent
                );

            filter: blur(2px);

            box-shadow:
                0 0 20px rgba(255,255,255,0.18);

            pointer-events: none;
        }


        /* =========================================================
        RESOLVEAI SYMBOL
        ========================================================= */

        .resolve-orb {
            position: relative;

            z-index: 2;

            width: 82px;
            height: 82px;

            margin:
                0 auto 28px auto;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 24px;

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.12),
                    rgba(255,255,255,0.025)
                );

            border:
                1px solid rgba(255,255,255,0.20);

            color: #ffffff;

            font-size: 32px;

            box-shadow:
                0 0 25px rgba(255,255,255,0.10),
                0 0 65px rgba(255,255,255,0.07),
                inset 0 1px 0 rgba(255,255,255,0.13);

            backdrop-filter: blur(20px);
        }


        /* =========================================================
        HERO TYPOGRAPHY
        ========================================================= */

        .resolve-hero-title {
            position: relative;

            z-index: 2;

            color: #f5f5f5;

            font-size:
                clamp(2.2rem, 4vw, 3.6rem);

            font-weight: 500;

            letter-spacing: -0.055em;

            line-height: 1.05;

            margin-bottom: 18px;

            text-shadow:
                0 0 35px rgba(255,255,255,0.06);
        }


        .resolve-hero-subtitle {
            position: relative;

            z-index: 2;

            max-width: 580px;

            margin: 0 auto;

            color: #858585;

            font-size: 0.96rem;

            line-height: 1.7;
        }


        /* =========================================================
        QUICK ACTION LABEL
        ========================================================= */

        .resolve-label {
            color: #666666;

            font-size: 0.67rem;

            font-weight: 600;

            letter-spacing: 0.12em;

            text-transform: uppercase;

            margin-bottom: 8px;
        }


        /* =========================================================
        QUICK ACTION BUTTONS
        ========================================================= */

        .stButton > button {
            min-height: 42px !important;

            border-radius: 11px !important;

            border:
                1px solid rgba(255,255,255,0.09) !important;

            background:
                linear-gradient(
                    180deg,
                    rgba(255,255,255,0.055),
                    rgba(255,255,255,0.018)
                ) !important;

            color: #a9a9a9 !important;

            font-size: 0.82rem !important;

            font-weight: 500 !important;

            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.025);

            transition:
                0.18s ease !important;
        }


        .stButton > button:hover {
            color: #ffffff !important;

            border-color:
                rgba(255,255,255,0.22) !important;

            background:
                rgba(255,255,255,0.075) !important;

            transform:
                translateY(-1px);
        }


        /* =========================================================
        PREMIUM CHAT COMPOSER
        ========================================================= */

        [data-testid="stChatInput"] {
            min-height: 68px;

            border-radius: 18px !important;

            border:
                1px solid rgba(255,255,255,0.18) !important;

            background:
                linear-gradient(
                    145deg,
                    rgba(38,38,38,0.90),
                    rgba(18,18,18,0.94)
                ) !important;

            box-shadow:
                0 18px 55px rgba(0,0,0,0.45),
                0 0 35px rgba(255,255,255,0.025),
                inset 0 1px 0 rgba(255,255,255,0.055);

            backdrop-filter:
                blur(25px);

            overflow: hidden;
        }


        [data-testid="stChatInput"] textarea {
            min-height: 54px !important;

            padding-top: 15px !important;

            color: #eeeeee !important;

            font-size: 0.93rem !important;

            background:
                transparent !important;
        }


        [data-testid="stChatInput"] textarea::placeholder {
            color: #666666 !important;
        }


        /* chat submit button */

        [data-testid="stChatInput"] button {
            border-radius: 11px !important;

            background:
                rgba(255,255,255,0.09) !important;

            border:
                1px solid rgba(255,255,255,0.10) !important;

            color: white !important;
        }


        [data-testid="stChatInput"] button:hover {
            background:
                rgba(255,255,255,0.16) !important;
        }


        /* =========================================================
        CHAT MESSAGES
        ========================================================= */

        [data-testid="stChatMessage"] {
            background:
                rgba(255,255,255,0.022) !important;

            border:
                1px solid rgba(255,255,255,0.065) !important;

            border-radius:
                16px !important;

            padding:
                1rem 1.15rem !important;

            margin-bottom:
                0.75rem !important;

            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.018);
        }


        /* =========================================================
        SUPPORT INTELLIGENCE
        ========================================================= */

        [data-testid="stMetric"] {
            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.045),
                    rgba(255,255,255,0.012)
                ) !important;

            border:
                1px solid rgba(255,255,255,0.075) !important;

            border-radius:
                14px !important;

            padding:
                16px !important;
        }


        [data-testid="stMetricLabel"] {
            color: #707070 !important;
        }


        [data-testid="stMetricValue"] {
            color: #eeeeee !important;

            font-size:
                1.35rem !important;
        }


        /* =========================================================
        ALERT / KNOWLEDGE CARDS
        ========================================================= */

        [data-testid="stAlert"] {
            border-radius:
                13px !important;

            background:
                rgba(255,255,255,0.028) !important;

            border:
                1px solid rgba(255,255,255,0.07) !important;

            color:
                #a9a9a9 !important;
        }


        /* =========================================================
        SIDEBAR POLISH
        ========================================================= */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #090909 0%,
                    #060606 100%
                ) !important;

            border-right:
                1px solid rgba(255,255,255,0.065);
        }


        [data-testid="stSidebar"] .stButton > button {
            justify-content: flex-start;

            padding-left: 16px;

            min-height: 43px !important;

            border-color:
                rgba(255,255,255,0.055) !important;

            background:
                rgba(255,255,255,0.018) !important;
        }


        [data-testid="stSidebar"] .stButton > button:hover {
            background:
                rgba(255,255,255,0.06) !important;

            border-color:
                rgba(255,255,255,0.13) !important;
        }


        /* =========================================================
        RESPONSIVE
        ========================================================= */

        @media (max-width: 900px) {

            .block-container {
                padding-left:
                    1rem !important;

                padding-right:
                    1rem !important;
            }

        }

    
        /* =========================================================
           STEP 7.3.6 — CENTERED AI WORKSPACE
        ========================================================= */


        /* =========================================
           HERO WORKSPACE WIDTH
        ========================================= */

        .resolve-hero {
            max-width: 900px !important;

            margin-left: auto !important;
            margin-right: auto !important;
        }


        /* =========================================
           COMPOSER SPACING
        ========================================= */

        .resolve-composer-space {
            height: 10px;
        }


        /* =========================================
           ACTIVE CONVERSATION HEADER
        ========================================= */

        .resolve-conversation-header {
            max-width: 900px;

            margin:
                1.5rem auto
                1.8rem auto;

            padding:
                14px 16px;

            display: flex;

            align-items: center;

            gap: 12px;

            border:
                1px solid
                rgba(255,255,255,0.07);

            border-radius: 14px;

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.035),
                    rgba(255,255,255,0.012)
                );

            box-shadow:
                inset 0 1px 0
                rgba(255,255,255,0.025);
        }


        .resolve-conversation-dot {
            width: 8px;
            height: 8px;

            flex-shrink: 0;

            border-radius: 50%;

            background: #eeeeee;

            box-shadow:
                0 0 14px
                rgba(255,255,255,0.45);
        }


        .resolve-conversation-title {
            color: #eeeeee;

            font-size: 0.9rem;

            font-weight: 500;
        }


        .resolve-conversation-subtitle {
            color: #626262;

            font-size: 0.7rem;

            margin-top: 2px;
        }


        /* =========================================
        SUPPORT INTELLIGENCE EMPTY STATE
        ========================================= */

        .resolve-intelligence-empty {
            width: 100%;
            max-width: 360px;

            margin-top: 18px;

            padding: 16px;

            display: flex;
            align-items: flex-start;
            gap: 12px;

            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 14px;

            background:
                linear-gradient(
                    145deg,
                    rgba(255, 255, 255, 0.035),
                    rgba(255, 255, 255, 0.012)
                );

            box-shadow:
                inset 0 1px 0 rgba(255, 255, 255, 0.025);
        }


        .resolve-intelligence-icon {
            width: 34px;
            height: 34px;

            display: flex;
            align-items: center;
            justify-content: center;

            flex-shrink: 0;

            border-radius: 10px;

            border: 1px solid rgba(255, 255, 255, 0.09);

            background: rgba(255, 255, 255, 0.04);

            color: #d5d5d5;

            font-size: 15px;
        }


        .resolve-intelligence-content {
            min-width: 0;
        }


        .resolve-intelligence-title {
            color: #d4d4d4;

            font-size: 0.78rem;
            font-weight: 600;

            line-height: 1.3;
        }


        .resolve-intelligence-status {
            margin-top: 3px;

            color: #8a8a8a;

            font-size: 0.68rem;
            font-weight: 500;
        }


        .resolve-intelligence-description {
            margin-top: 8px;

            color: #666666;

            font-size: 0.68rem;
            line-height: 1.5;
        }
        /* =========================================
           CENTER CHAT MESSAGES
        ========================================= */

        [data-testid="stChatMessage"] {
            max-width: 900px !important;

            margin-left: auto !important;
            margin-right: auto !important;
        }


        /* =========================================
           CENTER CHAT COMPOSER
        ========================================= */

        [data-testid="stChatInput"] {
            max-width: 900px !important;

            margin-left: auto !important;
            margin-right: auto !important;
        }


        /* =========================================
           MOBILE
        ========================================= */

        @media (max-width: 768px) {

            .resolve-intelligence-empty {
                margin-top: 14px;
                padding: 12px;
            }

            .resolve-conversation-header {
                margin-top: 10px;
                padding: 12px;
            }

            .resolve-conversation-title {
                font-size: 0.82rem;
            }

            .resolve-intelligence-description {
                font-size: 0.66rem;
            }

            .resolve-hero {
                margin-top: 1rem;
                padding-top: 2.5rem;
            }

            .resolve-hero-title {
                font-size: 2.3rem;
            }

            .resolve-hero-subtitle {
                font-size: 0.88rem;
            }
        }


        /* =========================================================
        STEP 7.3.8 — PREMIUM CONVERSATION UX
        ========================================================= */


        /* =========================================
        CONVERSATION TOP BAR
        ========================================= */

        .resolve-conversation-topbar {
            max-width: 1100px;

            margin:
                0 auto 28px auto;

            padding:
                13px 15px;

            display: flex;

            align-items: center;
            justify-content: space-between;

            gap: 16px;

            border:
                1px solid rgba(255,255,255,0.07);

            border-radius: 15px;

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.035),
                    rgba(255,255,255,0.012)
                );

            box-shadow:
                inset 0 1px 0
                rgba(255,255,255,0.025);
        }


        .resolve-conversation-identity {
            display: flex;

            align-items: center;

            gap: 11px;
        }


        .resolve-conversation-avatar {
            width: 36px;
            height: 36px;

            display: flex;

            align-items: center;
            justify-content: center;

            flex-shrink: 0;

            border-radius: 11px;

            color: #eeeeee;

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.09),
                    rgba(255,255,255,0.025)
                );

            border:
                1px solid rgba(255,255,255,0.11);

            box-shadow:
                0 0 22px
                rgba(255,255,255,0.035);
        }


        .resolve-conversation-name {
            color: #ededed;

            font-size: 0.86rem;

            font-weight: 550;
        }


        .resolve-conversation-state {
            display: flex;

            align-items: center;

            gap: 6px;

            color: #686868;

            font-size: 0.68rem;

            margin-top: 3px;
        }


        /* =========================================
        ACTIVE DOT
        ========================================= */

        .resolve-live-dot {
            display: inline-block;

            width: 6px;
            height: 6px;

            border-radius: 50%;

            background: #bdbdbd;

            box-shadow:
                0 0 8px
                rgba(255,255,255,0.35);
        }


        /* =========================================
        KNOWLEDGE STATUS BADGES
        ========================================= */

        .resolve-status-verified,
        .resolve-status-ai {
            padding:
                6px 10px;

            border-radius: 999px;

            font-size: 0.67rem;

            font-weight: 500;

            white-space: nowrap;
        }


        .resolve-status-verified {
            color: #dddddd;

            border:
                1px solid rgba(255,255,255,0.12);

            background:
                rgba(255,255,255,0.055);
        }


        .resolve-status-ai {
            color: #858585;

            border:
                1px solid rgba(255,255,255,0.07);

            background:
                rgba(255,255,255,0.025);
        }


        /* =========================================
        MESSAGE LABEL
        ========================================= */

        .resolve-message-label {
            color: #656565;

            font-size: 0.62rem;

            font-weight: 650;

            letter-spacing: 0.10em;

            margin-bottom: 8px;
        }


        /* =========================================
        CHAT MESSAGE POLISH
        ========================================= */

        [data-testid="stChatMessage"] {
            transition:
                border-color 0.18s ease,
                background 0.18s ease;
        }


        [data-testid="stChatMessage"]:hover {
            border-color:
                rgba(255,255,255,0.10) !important;

            background:
                rgba(255,255,255,0.03) !important;
        }


        /* =========================================
        CHAT TEXT
        ========================================= */

        [data-testid="stChatMessage"] p {
            color: #c7c7c7;

            font-size: 0.91rem;

            line-height: 1.65;
        }


        /* =========================================
        MOBILE TOP BAR
        ========================================= */

        @media (max-width: 768px) {

            .resolve-conversation-topbar {
                margin-bottom: 18px;
            }

            .resolve-status-verified,
            .resolve-status-ai {
                font-size: 0.61rem;

                padding:
                    5px 8px;
            }

            .resolve-conversation-avatar {
                width: 32px;
                height: 32px;
            }
        }


        /* =========================================================
        STEP 7.4 — PREMIUM TICKETS
        ========================================================= */


        /* =========================================
        TICKET HEADER
        ========================================= */

        .resolve-ticket-header {
            margin-top: 8px;
            margin-bottom: 24px;

            padding: 20px;

            display: flex;
            align-items: center;
            justify-content: space-between;

            gap: 20px;

            border-radius: 16px;

            border:
                1px solid rgba(255,255,255,0.08);

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.045),
                    rgba(255,255,255,0.012)
                );

            box-shadow:
                inset 0 1px 0
                rgba(255,255,255,0.025);
        }


        .resolve-ticket-id {
            color: #eeeeee;

            font-size: 1rem;

            font-weight: 600;

            letter-spacing: -0.02em;
        }


        .resolve-ticket-created {
            color: #656565;

            font-size: 0.72rem;

            margin-top: 5px;
        }


        .resolve-ticket-status {
            padding: 6px 11px;

            border-radius: 999px;

            color: #d5d5d5;

            font-size: 0.7rem;

            border:
                1px solid rgba(255,255,255,0.10);

            background:
                rgba(255,255,255,0.045);
        }


        /* =========================================
        TICKET METADATA
        ========================================= */

        .resolve-ticket-meta-label {
            color: #606060;

            font-size: 0.64rem;

            font-weight: 650;

            letter-spacing: 0.11em;

            margin-bottom: 6px;
        }


        .resolve-ticket-meta-value {
            color: #d8d8d8;

            font-size: 0.88rem;

            font-weight: 500;
        }


        /* =========================================
        TICKET SECTIONS
        ========================================= */

        .resolve-ticket-section-title {
            color: #ededed;

            font-size: 0.84rem;

            font-weight: 550;

            margin-bottom: 10px;
        }


        /* =========================================
        EMPTY TICKET STATE
        ========================================= */

        .resolve-ticket-empty {
            max-width: 520px;

            margin:
                6rem auto;

            text-align: center;

            padding: 32px;

            border:
                1px solid rgba(255,255,255,0.07);

            border-radius: 18px;

            background:
                rgba(255,255,255,0.018);
        }


        .resolve-ticket-empty-icon {
            width: 48px;
            height: 48px;

            margin:
                0 auto 18px auto;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 14px;

            color: #d5d5d5;

            background:
                rgba(255,255,255,0.04);

            border:
                1px solid rgba(255,255,255,0.08);
        }


        .resolve-ticket-empty-title {
            color: #e5e5e5;

            font-size: 1rem;

            font-weight: 550;
        }


        .resolve-ticket-empty-text {
            color: #666666;

            font-size: 0.78rem;

            margin-top: 7px;
        }
        /* =========================================================
        STEP 7.4.3 — TICKET ACTIONS
        ========================================================= */

        .resolve-action-button-space {
            height: 28px;
        }


        /* Ticket action selector */

        .resolve-ticket-header + .resolve-label {
            margin-top: 4px;
        }


        /* Improve ticket action area */

        [data-testid="stSelectbox"] label {
            color: #707070 !important;

            font-size: 0.72rem !important;

            font-weight: 500 !important;
        }


        /* Status update feedback */

        [data-testid="stToast"] {
            background:
                rgba(20,20,20,0.96) !important;

            border:
                1px solid rgba(255,255,255,0.10) !important;

            color: #eeeeee !important;

            border-radius: 12px !important;
        }


        /* =========================================================
        STEP 7.4.4 — PREMIUM TICKET QUEUE
        ========================================================= */


        /* =========================================
        QUEUE HEADER
        ========================================= */

        .resolve-queue-header {
            color: #5f5f5f;

            font-size: 0.62rem;

            font-weight: 650;

            letter-spacing: 0.10em;

            padding:
                0 8px 9px 8px;
        }


        /* =========================================
        TICKET ID
        ========================================= */

        .resolve-queue-ticket {
            min-height: 42px;

            display: flex;
            align-items: center;

            padding:
                0 8px;

            color: #dcdcdc;

            font-size: 0.78rem;

            font-weight: 550;

            letter-spacing: -0.01em;
        }


        /* =========================================
        QUEUE VALUES
        ========================================= */

        .resolve-queue-value {
            min-height: 42px;

            display: flex;
            align-items: center;

            padding:
                0 8px;

            color: #969696;

            font-size: 0.76rem;
        }


        /* =========================================
        STATUS
        ========================================= */

        .resolve-queue-status {
            min-height: 42px;

            display: flex;
            align-items: center;

            padding:
                0 8px;

            color: #b8b8b8;

            font-size: 0.72rem;

            font-weight: 500;
        }


        /* =========================================
        ROW DIVIDER
        ========================================= */

        .resolve-queue-divider {
            height: 1px;

            width: 100%;

            margin-bottom: 2px;

            background:
                rgba(255,255,255,0.055);
        }


        /* =========================================================
        STEP 7.4.5 — TICKET BADGES
        ========================================================= */


        /* =========================================
        BASE BADGE
        ========================================= */

        .resolve-ticket-badge {
            display: inline-flex;

            align-items: center;
            justify-content: center;

            min-height: 26px;

            padding:
                4px 9px;

            border-radius: 999px;

            font-size: 0.67rem;

            font-weight: 550;

            line-height: 1;

            white-space: nowrap;

            border:
                1px solid rgba(255,255,255,0.09);

            background:
                rgba(255,255,255,0.035);

            color: #a8a8a8;
        }


        /* =========================================
        QUEUE BADGE ALIGNMENT
        ========================================= */

        .resolve-queue-badge-wrapper {
            min-height: 42px;

            display: flex;

            align-items: center;

            padding:
                0 8px;
        }


        /* =========================================
        PRIORITY — CRITICAL
        ========================================= */

        .resolve-priority-critical {
            color: #f0f0f0;

            border-color:
                rgba(255,255,255,0.22);

            background:
                rgba(255,255,255,0.095);

            box-shadow:
                inset 0 1px 0
                rgba(255,255,255,0.055);
        }


        /* =========================================
        PRIORITY — HIGH
        ========================================= */

        .resolve-priority-high {
            color: #d6d6d6;

            border-color:
                rgba(255,255,255,0.16);

            background:
                rgba(255,255,255,0.065);
        }


        /* =========================================
        PRIORITY — MEDIUM
        ========================================= */

        .resolve-priority-medium {
            color: #ababab;

            border-color:
                rgba(255,255,255,0.10);

            background:
                rgba(255,255,255,0.035);
        }


        /* =========================================
        PRIORITY — LOW
        ========================================= */

        .resolve-priority-low {
            color: #797979;

            border-color:
                rgba(255,255,255,0.065);

            background:
                rgba(255,255,255,0.018);
        }


        /* =========================================
        STATUS — OPEN
        ========================================= */

        .resolve-status-open {
            color: #e1e1e1;

            border-color:
                rgba(255,255,255,0.17);

            background:
                rgba(255,255,255,0.065);
        }


        /* =========================================
        STATUS — IN PROGRESS
        ========================================= */

        .resolve-status-progress {
            color: #bdbdbd;

            border-color:
                rgba(255,255,255,0.12);

            background:
                rgba(255,255,255,0.04);
        }


        /* =========================================
        STATUS — RESOLVED
        ========================================= */

        .resolve-status-resolved {
            color: #8a8a8a;

            border-color:
                rgba(255,255,255,0.07);

            background:
                rgba(255,255,255,0.018);
        }


        /* =========================================
        FALLBACK
        ========================================= */

        .resolve-priority-default,
        .resolve-status-default {
            color: #888888;

            border-color:
                rgba(255,255,255,0.07);

            background:
                rgba(255,255,255,0.02);
        }

        /* =========================================================
        STEP 7.4.6 — SELECTED TICKET DETAILS
        ========================================================= */

        .resolve-detail-card {
            margin-bottom: 14px;

            padding: 20px;

            border-radius: 16px;

            border:
                1px solid rgba(255,255,255,0.075);

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.035),
                    rgba(255,255,255,0.010)
                );

            box-shadow:
                inset 0 1px 0
                rgba(255,255,255,0.022);

            transition:
                border-color 0.18s ease,
                background 0.18s ease;
        }


        .resolve-detail-card:hover {
            border-color:
                rgba(255,255,255,0.11);

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.045),
                    rgba(255,255,255,0.014)
                );
        }


        /* ---------- Header ---------- */

        .resolve-detail-card-header {
            display: flex;

            align-items: center;

            gap: 11px;

            margin-bottom: 15px;
        }


        .resolve-detail-icon {
            width: 34px;
            height: 34px;

            flex-shrink: 0;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 10px;

            color: #cfcfcf;

            font-size: 0.82rem;

            border:
                1px solid rgba(255,255,255,0.09);

            background:
                rgba(255,255,255,0.035);
        }


        .resolve-detail-title {
            color: #e5e5e5;

            font-size: 0.84rem;

            font-weight: 550;
        }


        .resolve-detail-caption {
            margin-top: 2px;

            color: #606060;

            font-size: 0.67rem;
        }


        /* ---------- Content ---------- */

        .resolve-detail-content {
            color: #a9a9a9;

            font-size: 0.84rem;

            line-height: 1.65;

            white-space: pre-wrap;

            overflow-wrap: anywhere;
        }


        .resolve-detail-muted {
            color: #737373;
        }


        /* ---------- Escalation ---------- */

        .resolve-detail-escalation {
            border-color:
                rgba(255,255,255,0.13);

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.052),
                    rgba(255,255,255,0.014)
                );
        }


        /* ---------- Mobile ---------- */

        @media (max-width: 768px) {

            .resolve-detail-card {
                padding: 16px;
            }

            .resolve-detail-content {
                font-size: 0.8rem;
            }
        }

        /* =========================================================
        STEP 7.4.7 — TICKET WORKFLOW POLISH
        ========================================================= */


        /* =========================================
        QUEUE SUMMARY
        ========================================= */

        .resolve-queue-summary {
            margin:
                16px 0 4px 0;

            padding:
                11px 14px;

            display: flex;

            align-items: center;
            justify-content: space-between;

            border-radius: 12px;

            border:
                1px solid rgba(255,255,255,0.055);

            background:
                rgba(255,255,255,0.015);

            color: #707070;

            font-size: 0.72rem;
        }


        .resolve-queue-count {
            color: #dedede;

            font-size: 0.82rem;

            font-weight: 600;

            margin-right: 4px;
        }


        .resolve-queue-total {
            color: #565656;

            font-size: 0.68rem;
        }


        /* =========================================
        SELECTED TICKET CONTEXT
        ========================================= */

        .resolve-selected-context {
            display: flex;

            align-items: center;

            flex-wrap: wrap;

            gap: 7px;

            margin:
                10px 0 18px 0;

            color: #626262;

            font-size: 0.7rem;
        }


        .resolve-selected-context strong {
            color: #bdbdbd;

            font-weight: 550;
        }


        /* =========================================
        FILTER SELECTS
        ========================================= */

        [data-testid="stSelectbox"] > div > div {
            transition:
                border-color 0.18s ease,
                background 0.18s ease;
        }


        /* =========================================
        TICKET QUEUE RESPONSIVE
        ========================================= */

        @media (max-width: 900px) {

            .resolve-queue-summary {
                margin-top: 12px;
            }

            .resolve-selected-context {
                line-height: 1.5;
            }
        }

        /* =========================================================
        STEP 7.5.1 — PREMIUM KNOWLEDGE WORKSPACE
        ========================================================= */


        /* =========================================
        COMPANY CARD
        ========================================= */

        .resolve-knowledge-company {
            margin:
                20px 0 28px 0;

            padding: 18px;

            display: flex;

            align-items: center;

            gap: 13px;

            border-radius: 16px;

            border:
                1px solid rgba(255,255,255,0.075);

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.04),
                    rgba(255,255,255,0.012)
                );
        }


        .resolve-knowledge-company-icon {
            width: 40px;
            height: 40px;

            flex-shrink: 0;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 12px;

            color: #e2e2e2;

            background:
                rgba(255,255,255,0.045);

            border:
                1px solid rgba(255,255,255,0.09);
        }


        .resolve-knowledge-company-title {
            color: #e8e8e8;

            font-size: 0.88rem;

            font-weight: 550;
        }


        .resolve-knowledge-company-caption {
            margin-top: 3px;

            color: #656565;

            font-size: 0.69rem;
        }


        .resolve-knowledge-verified {
            margin-left: auto;

            padding:
                6px 10px;

            border-radius: 999px;

            color: #cfcfcf;

            font-size: 0.66rem;

            white-space: nowrap;

            border:
                1px solid rgba(255,255,255,0.11);

            background:
                rgba(255,255,255,0.045);
        }


        /* =========================================
        POLICY LIBRARY
        ========================================= */

        .resolve-knowledge-policy-id,
        .resolve-knowledge-policy-title,
        .resolve-knowledge-category {
            min-height: 42px;

            display: flex;

            align-items: center;

            padding:
                0 8px;
        }


        .resolve-knowledge-policy-id {
            color: #777777;

            font-size: 0.7rem;

            font-weight: 550;
        }


        .resolve-knowledge-policy-title {
            color: #d2d2d2;

            font-size: 0.78rem;

            font-weight: 500;
        }


        .resolve-knowledge-category {
            color: #898989;

            font-size: 0.72rem;
        }


        /* =========================================
        SELECTED POLICY HEADER
        ========================================= */

        .resolve-knowledge-detail-header {
            margin:
                10px 0 22px 0;

            padding: 20px;

            display: flex;

            align-items: center;

            justify-content: space-between;

            gap: 18px;

            border-radius: 16px;

            border:
                1px solid rgba(255,255,255,0.085);

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.045),
                    rgba(255,255,255,0.012)
                );
        }


        .resolve-knowledge-detail-id {
            color: #666666;

            font-size: 0.65rem;

            font-weight: 600;

            letter-spacing: 0.08em;

            margin-bottom: 6px;
        }


        .resolve-knowledge-detail-title {
            color: #ededed;

            font-size: 1rem;

            font-weight: 550;

            letter-spacing: -0.02em;
        }


        /* =========================================
        KEYWORDS
        ========================================= */

        .resolve-knowledge-keywords {
            display: flex;

            flex-wrap: wrap;

            gap: 7px;
        }


        .resolve-knowledge-keyword {
            display: inline-flex;

            align-items: center;

            min-height: 25px;

            padding:
                4px 9px;

            border-radius: 999px;

            color: #8f8f8f;

            font-size: 0.66rem;

            border:
                1px solid rgba(255,255,255,0.075);

            background:
                rgba(255,255,255,0.025);
        }


        /* =========================================
        RETRIEVAL NOTE
        ========================================= */

        .resolve-knowledge-note {
            margin-top: 14px;

            padding: 16px 18px;

            border-radius: 14px;

            border:
                1px solid rgba(255,255,255,0.065);

            background:
                rgba(255,255,255,0.015);
        }


        .resolve-knowledge-note-title {
            color: #bdbdbd;

            font-size: 0.76rem;

            font-weight: 550;

            margin-bottom: 6px;
        }


        .resolve-knowledge-note-text {
            max-width: 760px;

            color: #676767;

            font-size: 0.71rem;

            line-height: 1.6;
        }


        /* =========================================
        MOBILE
        ========================================= */

        @media (max-width: 768px) {

            .resolve-knowledge-company {
                align-items: flex-start;
            }

            .resolve-knowledge-verified {
                font-size: 0.6rem;
            }

            .resolve-knowledge-detail-header {
                padding: 16px;
            }
        }

        /* =========================================================
        STEP 7.5.2 — KNOWLEDGE RETRIEVAL TESTER
        ========================================================= */


        /* =========================================
        TESTER INTRO
        ========================================= */

        .resolve-retrieval-heading {
            color: #ededed;

            font-size: 1.05rem;

            font-weight: 550;

            letter-spacing: -0.025em;

            margin-bottom: 6px;
        }


        .resolve-retrieval-description {
            max-width: 650px;

            color: #686868;

            font-size: 0.76rem;

            line-height: 1.6;

            margin-bottom: 18px;
        }


        /* =========================================
        TEXT AREA
        ========================================= */

        [data-testid="stTextArea"] textarea {
            color: #eeeeee !important;

            background:
                rgba(255,255,255,0.025) !important;

            border:
                1px solid rgba(255,255,255,0.09) !important;

            border-radius:
                14px !important;

            font-size:
                0.84rem !important;

            line-height: 1.55 !important;
        }


        [data-testid="stTextArea"] textarea:focus {
            border-color:
                rgba(255,255,255,0.20) !important;

            box-shadow:
                0 0 0 1px
                rgba(255,255,255,0.035) !important;
        }


        [data-testid="stTextArea"] textarea::placeholder {
            color: #555555 !important;
        }


        /* =========================================
        RESULT HEADER
        ========================================= */

        .resolve-retrieval-result-header {
            margin:
                18px 0 14px 0;

            padding:
                16px 18px;

            display: flex;

            align-items: center;

            justify-content: space-between;

            gap: 16px;

            border-radius: 14px;

            border:
                1px solid rgba(255,255,255,0.07);

            background:
                rgba(255,255,255,0.018);
        }


        .resolve-retrieval-result-title {
            color: #dddddd;

            font-size: 0.82rem;

            font-weight: 550;
        }


        .resolve-retrieval-result-caption {
            color: #5d5d5d;

            font-size: 0.66rem;

            margin-top: 3px;
        }


        /* =========================================
        CONFIDENCE BADGES
        ========================================= */

        .resolve-confidence-badge {
            display: inline-flex;

            align-items: center;

            padding:
                6px 10px;

            border-radius: 999px;

            font-size: 0.65rem;

            font-weight: 550;

            border:
                1px solid rgba(255,255,255,0.08);

            white-space: nowrap;
        }


        .resolve-confidence-strong {
            color: #f0f0f0;

            background:
                rgba(255,255,255,0.09);

            border-color:
                rgba(255,255,255,0.20);
        }


        .resolve-confidence-moderate {
            color: #c5c5c5;

            background:
                rgba(255,255,255,0.055);

            border-color:
                rgba(255,255,255,0.13);
        }


        .resolve-confidence-weak {
            color: #929292;

            background:
                rgba(255,255,255,0.025);

            border-color:
                rgba(255,255,255,0.08);
        }


        .resolve-confidence-none {
            color: #666666;

            background:
                rgba(255,255,255,0.012);

            border-color:
                rgba(255,255,255,0.05);
        }


        /* =========================================
        MATCHED POLICY
        ========================================= */

        .resolve-retrieval-policy {
            margin-top: 16px;

            padding: 20px;

            border-radius: 16px;

            border:
                1px solid rgba(255,255,255,0.085);

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.04),
                    rgba(255,255,255,0.012)
                );
        }


        .resolve-retrieval-policy-top {
            display: flex;

            align-items: center;

            justify-content: space-between;

            gap: 16px;

            margin-bottom: 16px;
        }


        .resolve-retrieval-policy-id {
            color: #626262;

            font-size: 0.63rem;

            font-weight: 600;

            letter-spacing: 0.08em;

            margin-bottom: 5px;
        }


        .resolve-retrieval-policy-title {
            color: #e1e1e1;

            font-size: 0.9rem;

            font-weight: 550;
        }


        .resolve-retrieval-policy-content {
            padding-top: 14px;

            border-top:
                1px solid rgba(255,255,255,0.055);

            color: #8d8d8d;

            font-size: 0.78rem;

            line-height: 1.65;

            white-space: pre-wrap;

            overflow-wrap: anywhere;
        }


        /* =========================================
        VERIFICATION RESULT
        ========================================= */

        .resolve-verification-result {
            margin-top: 12px;

            padding: 14px 16px;

            display: flex;

            gap: 11px;

            border-radius: 13px;

            border:
                1px solid rgba(255,255,255,0.065);

            background:
                rgba(255,255,255,0.015);
        }


        .resolve-verification-eligible {
            border-color:
                rgba(255,255,255,0.12);

            background:
                rgba(255,255,255,0.035);
        }


        .resolve-verification-symbol {
            width: 27px;
            height: 27px;

            flex-shrink: 0;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 8px;

            color: #c8c8c8;

            border:
                1px solid rgba(255,255,255,0.08);

            background:
                rgba(255,255,255,0.03);
        }


        .resolve-verification-title {
            color: #c7c7c7;

            font-size: 0.75rem;

            font-weight: 550;
        }


        .resolve-verification-text {
            max-width: 700px;

            margin-top: 4px;

            color: #666666;

            font-size: 0.68rem;

            line-height: 1.55;
        }


        /* =========================================
        NO MATCH
        ========================================= */

        .resolve-retrieval-no-match {
            margin-top: 16px;

            padding: 18px;

            display: flex;

            align-items: center;

            gap: 12px;

            border:
                1px solid rgba(255,255,255,0.06);

            border-radius: 14px;

            background:
                rgba(255,255,255,0.012);
        }


        .resolve-retrieval-no-match-icon {
            width: 34px;
            height: 34px;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 10px;

            color: #777777;

            border:
                1px solid rgba(255,255,255,0.06);
        }


        .resolve-retrieval-no-match-title {
            color: #aaaaaa;

            font-size: 0.76rem;

            font-weight: 550;
        }


        .resolve-retrieval-no-match-text {
            margin-top: 3px;

            color: #5c5c5c;

            font-size: 0.67rem;
        }


        /* =========================================
        TESTED MESSAGE
        ========================================= */

        .resolve-retrieval-tested-message {
            margin-top: 12px;

            padding: 15px 16px;

            color: #858585;

            font-size: 0.75rem;

            line-height: 1.55;

            border-radius: 13px;

            border:
                1px solid rgba(255,255,255,0.055);

            background:
                rgba(255,255,255,0.012);
        }

        /* =========================================================
        STEP 7.5.3 — RETRIEVAL QUALITY DIAGNOSTICS
        ========================================================= */


        /* =========================================
        DIAGNOSTIC CARD
        ========================================= */

        .resolve-diagnostic-card {
            margin-top: 10px;

            padding: 17px;

            border-radius: 14px;

            border:
                1px solid rgba(255,255,255,0.065);

            background:
                rgba(255,255,255,0.015);
        }


        .resolve-diagnostic-title {
            color: #d0d0d0;

            font-size: 0.78rem;

            font-weight: 550;
        }


        .resolve-diagnostic-caption {
            color: #5d5d5d;

            font-size: 0.65rem;

            margin-top: 3px;

            margin-bottom: 14px;
        }


        /* =========================================
        MATCHED KEYWORD ROW
        ========================================= */

        .resolve-diagnostic-keyword-row {
            min-height: 35px;

            display: flex;

            align-items: center;

            justify-content: space-between;

            gap: 12px;

            border-bottom:
                1px solid rgba(255,255,255,0.045);
        }


        .resolve-diagnostic-keyword-row:last-child {
            border-bottom: none;
        }


        .resolve-diagnostic-keyword {
            color: #999999;

            font-size: 0.72rem;
        }


        .resolve-diagnostic-weight {
            min-width: 30px;

            padding:
                3px 7px;

            text-align: center;

            border-radius: 999px;

            color: #d1d1d1;

            font-size: 0.64rem;

            border:
                1px solid rgba(255,255,255,0.08);

            background:
                rgba(255,255,255,0.03);
        }


        .resolve-diagnostic-empty {
            color: #5d5d5d;

            font-size: 0.7rem;

            padding:
                8px 0;
        }


        /* =========================================
        DIAGNOSTIC STAT
        ========================================= */

        .resolve-diagnostic-stat {
            min-height: 37px;

            display: flex;

            align-items: center;

            justify-content: space-between;

            gap: 12px;

            border-bottom:
                1px solid rgba(255,255,255,0.045);

            color: #696969;

            font-size: 0.7rem;
        }


        .resolve-diagnostic-stat:last-child {
            border-bottom: none;
        }


        .resolve-diagnostic-stat strong {
            color: #c5c5c5;

            font-size: 0.72rem;

            font-weight: 550;
        }


        /* =========================================
        CONFIDENCE THRESHOLD
        ========================================= */

        .resolve-threshold-card {
            margin-top: 14px;

            padding: 15px 17px;

            display: flex;

            align-items: flex-start;

            gap: 11px;

            border-radius: 13px;

            border:
                1px solid rgba(255,255,255,0.065);

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.025),
                    rgba(255,255,255,0.010)
                );
        }


        .resolve-threshold-symbol {
            width: 29px;
            height: 29px;

            flex-shrink: 0;

            display: flex;

            align-items: center;

            justify-content: center;

            border-radius: 9px;

            color: #bcbcbc;

            border:
                1px solid rgba(255,255,255,0.075);

            background:
                rgba(255,255,255,0.025);
        }


        .resolve-threshold-title {
            color: #bdbdbd;

            font-size: 0.73rem;

            font-weight: 550;
        }


        .resolve-threshold-description {
            max-width: 700px;

            margin-top: 4px;

            color: #616161;

            font-size: 0.67rem;

            line-height: 1.55;
        }
        /* =========================================================
        STEP 7.5.4 — KNOWLEDGE HEALTH & COVERAGE
        ========================================================= */

        .resolve-health-heading {
            color: #ededed;

            font-size: 1.05rem;

            font-weight: 550;

            letter-spacing: -0.025em;

            margin-bottom: 6px;
        }


        .resolve-health-description {
            max-width: 650px;

            color: #686868;

            font-size: 0.76rem;

            line-height: 1.6;

            margin-bottom: 20px;
        }


        /* =========================================
        SECTION TITLES
        ========================================= */

        .resolve-health-card-title {
            color: #cccccc;

            font-size: 0.8rem;

            font-weight: 550;

            margin-bottom: 4px;
        }


        .resolve-health-card-caption {
            color: #5f5f5f;

            font-size: 0.66rem;

            line-height: 1.5;

            margin-bottom: 14px;
        }


        /* =========================================
        HEALTH SUMMARY
        ========================================= */

        .resolve-health-summary-card {
            padding: 15px 17px;

            border-radius: 14px;

            border:
                1px solid rgba(255,255,255,0.065);

            background:
                rgba(255,255,255,0.015);
        }


        .resolve-health-stat {
            min-height: 42px;

            display: flex;

            align-items: center;

            justify-content: space-between;

            gap: 14px;

            color: #707070;

            font-size: 0.7rem;

            border-bottom:
                1px solid rgba(255,255,255,0.045);
        }


        .resolve-health-stat:last-child {
            border-bottom: none;
        }


        .resolve-health-stat strong {
            color: #c8c8c8;

            font-size: 0.75rem;

            font-weight: 550;
        }


        /* =========================================
        POLICY COVERAGE ROW
        ========================================= */

        .resolve-health-policy-row {
            min-height: 64px;

            margin-top: 8px;

            padding: 12px 14px;

            display: flex;

            align-items: center;

            justify-content: space-between;

            gap: 16px;

            border-radius: 12px;

            border:
                1px solid rgba(255,255,255,0.055);

            background:
                rgba(255,255,255,0.012);
        }


        .resolve-health-policy-id {
            color: #5f5f5f;

            font-size: 0.61rem;

            font-weight: 600;

            letter-spacing: 0.07em;
        }


        .resolve-health-policy-title {
            color: #bdbdbd;

            font-size: 0.75rem;

            font-weight: 500;

            margin-top: 3px;
        }


        .resolve-health-policy-category {
            color: #5f5f5f;

            font-size: 0.64rem;

            margin-top: 3px;
        }


        .resolve-health-keyword-count {
            padding: 5px 9px;

            border-radius: 999px;

            white-space: nowrap;

            color: #8a8a8a;

            font-size: 0.63rem;

            border:
                1px solid rgba(255,255,255,0.07);

            background:
                rgba(255,255,255,0.02);
        }


        /* =========================================
        SHARED KEYWORDS
        ========================================= */

        .resolve-shared-keyword-row {
            min-height: 42px;

            padding:
                8px 12px;

            display: flex;

            align-items: center;

            justify-content: space-between;

            gap: 18px;

            border-bottom:
                1px solid rgba(255,255,255,0.045);
        }


        .resolve-shared-keyword {
            color: #a5a5a5;

            font-size: 0.71rem;
        }


        .resolve-shared-policy {
            color: #606060;

            font-size: 0.65rem;

            text-align: right;
        }


        /* =========================================
        HEALTHY STATE
        ========================================= */

        .resolve-health-good {
            margin-top: 10px;

            padding: 15px;

            display: flex;

            align-items: center;

            gap: 11px;

            border-radius: 13px;

            border:
                1px solid rgba(255,255,255,0.065);

            background:
                rgba(255,255,255,0.015);
        }


        .resolve-health-good-symbol {
            width: 29px;
            height: 29px;

            flex-shrink: 0;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 9px;

            color: #bdbdbd;

            border:
                1px solid rgba(255,255,255,0.075);

            background:
                rgba(255,255,255,0.025);
        }


        .resolve-health-good-title {
            color: #bdbdbd;

            font-size: 0.72rem;

            font-weight: 550;
        }


        .resolve-health-good-text {
            color: #606060;

            font-size: 0.66rem;

            margin-top: 3px;

            line-height: 1.5;
        }


        /* =========================================
        MOBILE
        ========================================= */

        @media (max-width: 768px) {

            .resolve-health-policy-row {
                align-items: flex-start;
            }

            .resolve-shared-keyword-row {
                align-items: flex-start;
            }
        }

        /* =========================================================
        STEP 7.5.5.2 — RETRIEVAL CONFLICT ANALYSIS
        ========================================================= */

        .resolve-conflict-heading {
            color: #ededed;
            font-size: 1.05rem;
            font-weight: 550;
            letter-spacing: -0.025em;
            margin-bottom: 6px;
        }

        .resolve-conflict-description {
            max-width: 680px;
            color: #686868;
            font-size: 0.76rem;
            line-height: 1.6;
            margin-bottom: 20px;
        }


        /* =========================================
        STATUS
        ========================================= */

        .resolve-conflict-status {
            margin-top: 14px;
            padding: 15px 16px;

            display: flex;
            align-items: center;
            gap: 12px;

            border-radius: 14px;

            border:
                1px solid rgba(255,255,255,0.07);

            background:
                rgba(255,255,255,0.018);
        }

        .resolve-conflict-status-symbol {
            width: 32px;
            height: 32px;

            flex-shrink: 0;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 10px;

            color: #c9c9c9;

            border:
                1px solid rgba(255,255,255,0.08);

            background:
                rgba(255,255,255,0.025);
        }

        .resolve-conflict-status-title {
            color: #c8c8c8;
            font-size: 0.76rem;
            font-weight: 600;
        }

        .resolve-conflict-status-text {
            color: #676767;
            font-size: 0.67rem;
            line-height: 1.5;
            margin-top: 3px;
        }

        .resolve-conflict-danger {
            border-color:
                rgba(255,255,255,0.13);
        }

        .resolve-conflict-warning {
            border-color:
                rgba(255,255,255,0.10);
        }

        .resolve-conflict-clear {
            border-color:
                rgba(255,255,255,0.065);
        }


        /* =========================================
        BEST MATCH
        ========================================= */

        .resolve-conflict-best {
            padding: 17px;

            border-radius: 15px;

            border:
                1px solid rgba(255,255,255,0.08);

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.035),
                    rgba(255,255,255,0.012)
                );
        }

        .resolve-conflict-best-top {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 18px;
        }

        .resolve-conflict-policy-id {
            color: #5e5e5e;
            font-size: 0.61rem;
            font-weight: 600;
            letter-spacing: 0.07em;
        }

        .resolve-conflict-policy-title {
            color: #d0d0d0;
            font-size: 0.9rem;
            font-weight: 550;
            margin-top: 4px;
        }

        .resolve-conflict-policy-category {
            color: #646464;
            font-size: 0.65rem;
            margin-top: 4px;
        }

        .resolve-conflict-score {
            min-width: 54px;

            color: #e0e0e0;

            font-size: 1.25rem;
            font-weight: 550;

            text-align: right;
        }

        .resolve-conflict-score span {
            display: block;

            color: #575757;

            font-size: 0.56rem;
            font-weight: 500;
        }

        .resolve-conflict-confidence {
            margin-top: 13px;

            color: #727272;

            font-size: 0.66rem;
        }


        /* =========================================
        MATCHED KEYWORDS
        ========================================= */

        .resolve-conflict-subheading {
            margin-top: 14px;
            margin-bottom: 8px;

            color: #777777;

            font-size: 0.66rem;
            font-weight: 600;

            letter-spacing: 0.06em;

            text-transform: uppercase;
        }

        .resolve-conflict-keywords {
            display: flex;
            flex-wrap: wrap;
            gap: 7px;
        }

        .resolve-conflict-keyword {
            padding: 6px 9px;

            display: flex;
            align-items: center;
            gap: 7px;

            border-radius: 9px;

            border:
                1px solid rgba(255,255,255,0.065);

            background:
                rgba(255,255,255,0.018);

            color: #858585;

            font-size: 0.65rem;
        }

        .resolve-conflict-keyword strong {
            color: #b8b8b8;
            font-weight: 550;
        }


        /* =========================================
        COMPETING CANDIDATES
        ========================================= */

        .resolve-conflict-candidate {
            margin-top: 8px;

            padding: 14px;

            border-radius: 13px;

            border:
                1px solid rgba(255,255,255,0.06);

            background:
                rgba(255,255,255,0.012);
        }

        .resolve-conflict-candidate-main {
            display: flex;
            justify-content: space-between;
            gap: 16px;
        }

        .resolve-conflict-candidate-title {
            color: #b8b8b8;
            font-size: 0.76rem;
            font-weight: 520;
            margin-top: 3px;
        }

        .resolve-conflict-candidate-score {
            color: #bdbdbd;
            font-size: 0.92rem;
            font-weight: 550;
        }

        .resolve-conflict-candidate-meta {
            color: #626262;
            font-size: 0.62rem;
            margin-top: 7px;
        }

        .resolve-conflict-mini-keywords {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-top: 9px;
        }

        .resolve-conflict-mini-keyword {
            padding: 4px 7px;

            border-radius: 7px;

            color: #747474;

            font-size: 0.59rem;

            border:
                1px solid rgba(255,255,255,0.05);
        }


        /* =========================================
        CLEAR / GUIDANCE / EMPTY STATES
        ========================================= */

        .resolve-conflict-clear-card,
        .resolve-conflict-guidance,
        .resolve-conflict-empty {
            margin-top: 9px;

            padding: 15px;

            display: flex;
            align-items: center;
            gap: 11px;

            border-radius: 13px;

            border:
                1px solid rgba(255,255,255,0.06);

            background:
                rgba(255,255,255,0.014);
        }

        .resolve-conflict-clear-symbol,
        .resolve-conflict-guidance-symbol,
        .resolve-conflict-empty-symbol {
            width: 30px;
            height: 30px;

            flex-shrink: 0;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 9px;

            color: #b7b7b7;

            border:
                1px solid rgba(255,255,255,0.07);

            background:
                rgba(255,255,255,0.02);
        }

        .resolve-conflict-clear-title,
        .resolve-conflict-guidance-title,
        .resolve-conflict-empty-title {
            color: #bcbcbc;
            font-size: 0.72rem;
            font-weight: 550;
        }

        .resolve-conflict-clear-text,
        .resolve-conflict-guidance-text,
        .resolve-conflict-empty-text {
            color: #626262;
            font-size: 0.65rem;
            line-height: 1.5;
            margin-top: 3px;
        }


        /* =========================================
        MOBILE
        ========================================= */

        @media (max-width: 768px) {

            .resolve-conflict-best-top,
            .resolve-conflict-candidate-main {
                gap: 10px;
            }

            .resolve-conflict-status,
            .resolve-conflict-guidance,
            .resolve-conflict-clear-card,
            .resolve-conflict-empty {
                align-items: flex-start;
            }
        }
        /* =========================================================
        STEP 7.5.5.4 — LIVE RETRIEVAL RELIABILITY
        ========================================================= */

        .resolve-live-conflict,
        .resolve-live-retrieval {
            margin-top: 8px;
            padding: 13px;

            display: flex;
            align-items: center;
            gap: 10px;

            border-radius: 12px;

            border:
                1px solid rgba(255,255,255,0.07);

            background:
                rgba(255,255,255,0.015);
        }


        .resolve-live-conflict {
            border-color:
                rgba(255,255,255,0.12);
        }


        .resolve-live-conflict-icon,
        .resolve-live-retrieval-icon {
            width: 29px;
            height: 29px;

            flex-shrink: 0;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 9px;

            color: #c5c5c5;

            background:
                rgba(255,255,255,0.025);

            border:
                1px solid rgba(255,255,255,0.07);
        }


        .resolve-live-conflict-title,
        .resolve-live-retrieval-title {
            color: #bdbdbd;

            font-size: 0.7rem;

            font-weight: 600;
        }


        .resolve-live-conflict-text,
        .resolve-live-retrieval-text {
            color: #626262;

            font-size: 0.62rem;

            line-height: 1.45;

            margin-top: 2px;
        }


        .resolve-live-competitor-label {
            color: #555555;

            font-size: 0.58rem;

            font-weight: 600;

            letter-spacing: 0.08em;

            margin-top: 13px;

            margin-bottom: 6px;
        }


        .resolve-live-competitor {
            padding: 9px 10px;

            margin-bottom: 5px;

            border-radius: 9px;

            border:
                1px solid rgba(255,255,255,0.05);

            background:
                rgba(255,255,255,0.01);
        }


        .resolve-live-competitor-title {
            color: #999999;

            font-size: 0.65rem;

            font-weight: 500;
        }


        .resolve-live-competitor-meta {
            color: #555555;

            font-size: 0.58rem;

            margin-top: 2px;
        }

        /* =========================================================
        STEP 7.5.6.3 — RETRIEVAL DECISION TRACE
        ========================================================= */

        .resolve-trace-card {
            margin-top: 8px;
            margin-bottom: 14px;

            padding: 15px;

            border-radius: 14px;

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.045),
                    rgba(255,255,255,0.015)
                );

            border:
                1px solid rgba(255,255,255,0.08);
        }


        .resolve-trace-eligible {
            border-color:
                rgba(255,255,255,0.15);
        }


        .resolve-trace-blocked {
            border-color:
                rgba(255,255,255,0.13);
        }


        .resolve-trace-neutral {
            border-color:
                rgba(255,255,255,0.08);
        }


        .resolve-trace-top {
            display: flex;

            align-items: center;

            gap: 10px;
        }


        .resolve-trace-icon {
            width: 30px;
            height: 30px;

            display: flex;

            align-items: center;
            justify-content: center;

            flex-shrink: 0;

            border-radius: 9px;

            background:
                rgba(255,255,255,0.06);

            border:
                1px solid rgba(255,255,255,0.08);

            color: #eeeeee;

            font-size: 0.82rem;
        }


        .resolve-trace-title {
            color: #eeeeee;

            font-size: 0.86rem;

            font-weight: 600;
        }


        .resolve-trace-status {
            margin-top: 2px;

            color: #737373;

            font-size: 0.72rem;
        }


        .resolve-trace-reason {
            margin-top: 12px;

            color: #929292;

            font-size: 0.76rem;

            line-height: 1.55;
        }


        .resolve-trace-policy {
            margin-top: 12px;

            padding: 12px;

            border-radius: 11px;

            background:
                rgba(255,255,255,0.025);

            border:
                1px solid rgba(255,255,255,0.065);
        }


        .resolve-trace-small-label {
            margin-top: 12px;
            margin-bottom: 7px;

            color: #626262;

            font-size: 0.62rem;

            font-weight: 600;

            letter-spacing: 0.10em;
        }


        .resolve-trace-policy
        .resolve-trace-small-label {
            margin-top: 0;
        }


        .resolve-trace-policy-title {
            color: #dcdcdc;

            font-size: 0.82rem;

            font-weight: 500;
        }


        .resolve-trace-policy-meta {
            margin-top: 3px;

            color: #666666;

            font-size: 0.69rem;
        }


        .resolve-trace-evidence-list {
            display: flex;

            flex-direction: column;

            gap: 6px;
        }


        .resolve-trace-evidence {
            display: flex;

            align-items: center;

            justify-content: space-between;

            padding: 8px 10px;

            border-radius: 9px;

            background:
                rgba(255,255,255,0.025);

            border:
                1px solid rgba(255,255,255,0.055);

            color: #a6a6a6;

            font-size: 0.72rem;
        }


        .resolve-trace-weight {
            color: #e1e1e1;

            font-weight: 600;
        }


        .resolve-trace-score-gap {
            display: flex;

            justify-content: space-between;

            align-items: center;

            margin-top: 10px;

            padding-top: 10px;

            border-top:
                1px solid rgba(255,255,255,0.055);

            color: #737373;

            font-size: 0.71rem;
        }


        .resolve-trace-score-gap strong {
            color: #d0d0d0;

            font-weight: 600;
        }

        /* =========================================================
        STEP 7.5.6.4 — RETRIEVAL TRACE HISTORY
        ========================================================= */

        .resolve-trace-history-item {
            margin-bottom: 8px;
            padding: 11px;

            border-radius: 11px;

            background:
                rgba(255,255,255,0.022);

            border:
                1px solid rgba(255,255,255,0.06);
        }


        .resolve-trace-history-top {
            display: flex;
            align-items: flex-start;
            gap: 8px;
        }


        .resolve-trace-history-status {
            width: 24px;
            height: 24px;

            display: flex;
            align-items: center;
            justify-content: center;

            flex-shrink: 0;

            border-radius: 7px;

            background:
                rgba(255,255,255,0.05);

            color: #d8d8d8;

            font-size: 0.68rem;
        }


        .resolve-trace-history-main {
            flex: 1;
            min-width: 0;
        }


        .resolve-trace-history-policy {
            color: #d5d5d5;

            font-size: 0.74rem;

            font-weight: 600;
        }


        .resolve-trace-history-message {
            margin-top: 3px;

            color: #737373;

            font-size: 0.67rem;

            line-height: 1.4;
        }


        .resolve-trace-history-type {
            color: #888888;

            font-size: 0.62rem;

            white-space: nowrap;
        }


        .resolve-trace-history-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;

            margin-top: 8px;
            padding-top: 7px;

            border-top:
                1px solid rgba(255,255,255,0.045);

            color: #626262;

            font-size: 0.61rem;
        }


                
        /* =========================================================
        RETRIEVAL HEALTH
        ========================================================= */

        .resolve-retrieval-health {
            display: flex;
            gap: 12px;
            align-items: flex-start;

            padding: 14px;

            margin-top: 10px;
            margin-bottom: 12px;

            border-radius: 14px;

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.045),
                    rgba(255,255,255,0.015)
                );

            border:
                1px solid rgba(255,255,255,0.08);
        }


        .resolve-retrieval-health-icon {
            width: 30px;
            height: 30px;

            flex-shrink: 0;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 9px;

            background:
                rgba(255,255,255,0.06);

            border:
                1px solid rgba(255,255,255,0.09);

            color: #eeeeee;

            font-size: 0.85rem;
        }


        .resolve-retrieval-health-title {
            color: #eeeeee;

            font-size: 0.82rem;
            font-weight: 600;

            margin-bottom: 4px;
        }


        .resolve-retrieval-health-text {
            color: #777777;

            font-size: 0.72rem;
            line-height: 1.5;
        }


        .resolve-retrieval-health-grid {
            display: grid;

            grid-template-columns:
                repeat(2, 1fr);

            gap: 8px;

            margin-top: 8px;
        }


        .resolve-retrieval-health-stat {
            padding: 10px;

            border-radius: 11px;

            background:
                rgba(255,255,255,0.025);

            border:
                1px solid rgba(255,255,255,0.06);
        }


        .resolve-retrieval-health-value {
            color: #eeeeee;

            font-size: 1rem;
            font-weight: 600;
        }


        .resolve-retrieval-health-label {
            margin-top: 2px;

            color: #666666;

            font-size: 0.66rem;

            text-transform: uppercase;

            letter-spacing: 0.06em;
        }
        /* =========================================================
        SIDEBAR SYSTEM STATUS — FINAL POLISH
        ========================================================= */

        /* Make sidebar content use available viewport height */

        [data-testid="stSidebar"] [data-testid="stSidebarContent"] {
            min-height: 100vh;
        }


        /* ---------------------------------------------------------
        SYSTEM STATUS CARD
        --------------------------------------------------------- */

        .sidebar-footer {
            margin-top: 32px;

            padding: 13px 14px;

            display: flex;
            align-items: center;

            gap: 11px;

            border-radius: 13px;

            border:
                1px solid rgba(255,255,255,0.07);

            background:
                linear-gradient(
                    145deg,
                    rgba(255,255,255,0.035),
                    rgba(255,255,255,0.012)
                );

            box-shadow:
                inset 0 1px 0 rgba(255,255,255,0.025);

            transition:
                border-color 0.18s ease,
                background 0.18s ease;
        }


        .sidebar-footer:hover {
            border-color:
                rgba(255,255,255,0.11);

            background:
                rgba(255,255,255,0.035);
        }


        /* ---------------------------------------------------------
        OPERATIONAL STATUS DOT
        --------------------------------------------------------- */

        .sidebar-status-dot {
            width: 8px;
            height: 8px;

            flex-shrink: 0;

            border-radius: 50%;

            background: #58c987;

            box-shadow:
                0 0 0 3px rgba(88,201,135,0.08),
                0 0 12px rgba(88,201,135,0.30);
        }


        /* ---------------------------------------------------------
        STATUS TYPOGRAPHY
        --------------------------------------------------------- */

        .sidebar-status-title {
            color: #d8d8d8;

            font-size: 0.76rem;

            font-weight: 550;

            line-height: 1.2;
        }


        .sidebar-status-text {
            margin-top: 3px;

            color: #646464;

            font-size: 0.65rem;

            line-height: 1.25;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )