import streamlit as st
import time
import random

st.set_page_config(page_title="Birthday Celebration", page_icon="🎂")

def main():
    st.markdown("""
        <style>
        .main {
            background-color: #fff5e6;
        }
        h1 {
            color: #d35400;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("🎂 A Special Message...")

    if "unlocked" not in st.session_state:
        st.session_state.unlocked = False

    if not st.session_state.unlocked:
        if st.button("Click to open your card"):
            with st.spinner("Calculating niqqa energy..."):
                time.sleep(1.5)
                st.session_state.unlocked = True
                st.rerun()
    else:
        st.balloons()
        st.header("Happy New Year Niqqa!")

        col1, col2 = st.columns([1, 2])

        monke = random.choice(["🐒", "🙈", "🙉", "🙊"])
        
        with col1:
            st.markdown("""
                <style>
                .stApp {
                    background: linear-gradient(-45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
                    background-size: 400% 400%;
                    animation: gradient 15s ease infinite;
                    height: 100vh;
                }

                @keyframes gradient {
                    0% {
                        background-position: 0% 50%;
                    }
                    50% {
                        background-position: 100% 50%;
                    }
                    100% {
                        background-position: 0% 50%;
                    }
                }
                
                /* Making text readable against the chaos */
                h1, h2, h3, p, span {
                    color: white !important;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                }
                </style>
                """, unsafe_allow_html=True)
            
            st.markdown(f"# {monke}")
            
        with col2:
            st.subheader("To the world's greatest cotton picker.")
            st.write("You ducking monke.")

        # An interactive "Ginger Meter" just for fun
        st.divider()
        ginger_level = st.slider("Niqa Intensity Today", 0, 100, 85)
        
        if ginger_level > 90:
            st.warning("Warning: Critical Niqqa Levels Detected. Go pick up cotton.")

        if st.button("Celebrate Again"):
            st.snow()

if __name__ == "__main__":
    main()