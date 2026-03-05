import streamlit as st
import os
from main import game_builder_agent  # Import your compiled LangGraph

# Page Config
st.set_page_config(page_title="Agentic Code Orchestrator", page_icon="🤖", layout="wide")

st.title("🤖 Agentic Code Orchestrator")
st.markdown("Automating the transition from **User Intent** to **Executable Phaser.js Code**.")

# Sidebar for Configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    model_choice = st.selectbox("LLM Engine", ["Gemini 1.5 Pro", "Gemini 1.5 Flash"])
    st.info("This system uses a multi-agent DAG (Inquisitor -> Architect -> Builder) to ensure code integrity.")

# User Input
user_prompt = st.text_area("Describe the game mechanics:", 
                            placeholder="Example: A platformer where a ninja collects coins and avoids spikes...")

if st.button("Generate Executable Code 🚀"):
    if not user_prompt:
        st.warning("Please enter a game idea.")
    else:
        # 1. Start the Agentic Workflow
        with st.status("🚀 Orchestrating Agents...", expanded=True) as status:
            st.write("🕵️ **Inquisitor Node:** Refining requirements...")
            # We invoke your graph here
            # result = game_builder_agent.invoke({"user_idea": user_prompt})
            
            # Simulate a brief delay or show node progress
            st.write("📐 **Architect Node:** Designing technical blueprint...")
            st.write("🛠️ **Builder Node:** Generating Phaser.js implementation...")
            
            # For demonstration, assume final_state is returned from your graph
            result = game_builder_agent.invoke({"user_idea": user_prompt})
            status.update(label="Build Complete!", state="complete", expanded=False)

        # 2. Display the Output
        st.success("Generation Successful!")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("📄 Generated Code")
            # Assuming your graph returns a dict with 'html_code'
            tab1, tab2 = st.tabs(["index.html", "game.js"])
            with tab1:
                st.code(result.get("html_code", ""), language="html")
            with tab2:
                st.code(result.get("js_code", "// No JS generated"), language="javascript")

        with col2:
            st.subheader("📦 Export")
            st.download_button(
                label="Download ZIP Archive",
                data="...", # Add logic to zip your generated files
                file_name="game_project.zip",
                mime="application/zip"
            )