import streamlit as st
from example_task_flow import create_startup_analysis_flow

def format_result(result_text):
    # Extract task number, description and result
    try:
        # Split into parts
        parts = result_text.split("\nResult: ")
        task_info = parts[0]  # Contains "Task X: description"
        result_content = parts[1]
        
        # Extract task number and description
        task_num = task_info.split(":")[0].strip()  # "Task X"
        task_desc = task_info.split(":")[1].strip()
        
        return task_desc, result_content
    except:
        return "Unknown Task", result_text

def main():
    st.set_page_config(
        page_title="ThinkTank AI - Startup Idea Analyzer",
        page_icon="🚀",
        layout="wide"
    )

    # Custom CSS
    st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main-title {
        text-align: center;
        margin-bottom: 2rem;
        color: #1f1f1f;
        font-weight: 700;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
        font-size: 1.1rem;
    }
    .results-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border: 1px solid #eee;
    }
    .section-title {
        color: #2c3e50;
        font-size: 1.3rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    .expander-content {
        font-size: 0.95rem;
        line-height: 1.6;
        color: #444;
        padding: 0.5rem 0;
    }
    div[data-testid="stExpander"] {
        border: 1px solid #f0f0f0;
        border-radius: 8px;
        margin-bottom: 0.5rem;
    }
    div[data-testid="stExpander"] > div:first-child {
        background-color: #f8f9fa;
        padding: 0.5rem;
    }
    .success-message {
        text-align: center;
        color: #28a745;
        padding: 1rem;
        border-radius: 8px;
        background-color: #f8f9fa;
        margin-top: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<h1 class="main-title">🚀 ThinkTank AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Transform your startup idea into actionable insights</p>', unsafe_allow_html=True)

    # Input section
    startup_idea = st.text_area(
        "✍️ Enter your startup idea",
        height=120,
        placeholder="Describe your startup idea in detail...",
        help="Be specific about your target market, core features, and value proposition"
    )

    # Analysis button
    if st.button("Analyze Startup Idea", type="primary"):
        if not startup_idea:
            st.error("Please enter a startup idea to analyze")
            return

        # Show progress
        progress_text = "Analysis in progress..."
        progress_bar = st.progress(0)
        
        with st.spinner(progress_text):
            # Run the analysis
            results = create_startup_analysis_flow(startup_idea)
            
            # Create columns for displaying results
            col1, col2 = st.columns(2)
            
            # Process results
            formatted_results = {}
            total_tasks = len(results)
            for i, result in enumerate(results):
                task_desc, content = format_result(result)
                formatted_results[task_desc] = content
                progress_bar.progress((i + 1) / total_tasks)

            # Display results in organized sections with improved styling
            with col1:
                # Market & Customer Analysis Card
                st.markdown('<div class="results-card">', unsafe_allow_html=True)
                st.markdown('<p class="section-title">📊 Market & Customer Analysis</p>', unsafe_allow_html=True)
                if "Analyze market size, trends, and competitor landscape" in formatted_results:
                    with st.expander("📈 Market Research"):
                        st.markdown('<div class="expander-content">' + 
                                  formatted_results["Analyze market size, trends, and competitor landscape"] +
                                  '</div>', unsafe_allow_html=True)
                
                if "Define target customers and their needs" in formatted_results:
                    with st.expander("👥 Customer Personas"):
                        st.markdown('<div class="expander-content">' + 
                                  formatted_results["Define target customers and their needs"] +
                                  '</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Business Strategy Card
                st.markdown('<div class="results-card">', unsafe_allow_html=True)
                st.markdown('<p class="section-title">💼 Business Strategy</p>', unsafe_allow_html=True)
                if "Design comprehensive business model" in formatted_results:
                    with st.expander("📑 Business Model"):
                        st.markdown('<div class="expander-content">' + 
                                  formatted_results["Design comprehensive business model"] +
                                  '</div>', unsafe_allow_html=True)
                
                if "Identify key differentiators and advantages" in formatted_results:
                    with st.expander("⚡ Competitive Edge"):
                        st.markdown('<div class="expander-content">' + 
                                  formatted_results["Identify key differentiators and advantages"] +
                                  '</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                # Technical & Financial Card
                st.markdown('<div class="results-card">', unsafe_allow_html=True)
                st.markdown('<p class="section-title">🔧 Technical & Financial</p>', unsafe_allow_html=True)
                if "Evaluate technical and financial feasibility" in formatted_results:
                    with st.expander("📊 Feasibility Study"):
                        st.markdown('<div class="expander-content">' + 
                                  formatted_results["Evaluate technical and financial feasibility"] +
                                  '</div>', unsafe_allow_html=True)
                
                if "Recommend optimal technology stack" in formatted_results:
                    with st.expander("💻 Tech Stack"):
                        st.markdown('<div class="expander-content">' + 
                                  formatted_results["Recommend optimal technology stack"] +
                                  '</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Go-to-Market Card
                st.markdown('<div class="results-card">', unsafe_allow_html=True)
                st.markdown('<p class="section-title">🎯 Go-to-Market</p>', unsafe_allow_html=True)
                if "Develop revenue generation strategies" in formatted_results:
                    with st.expander("💰 Revenue Model"):
                        st.markdown('<div class="expander-content">' + 
                                  formatted_results["Develop revenue generation strategies"] +
                                  '</div>', unsafe_allow_html=True)
                
                if "Create launch and market entry strategy" in formatted_results:
                    with st.expander("🚀 Launch Plan"):
                        st.markdown('<div class="expander-content">' + 
                                  formatted_results["Create launch and market entry strategy"] +
                                  '</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            # Investment Summary Card
            st.markdown('<div class="results-card">', unsafe_allow_html=True)
            st.markdown('<p class="section-title">💰 Investment Summary</p>', unsafe_allow_html=True)
            if "Create compelling pitch materials" in formatted_results:
                with st.expander("📊 Investor Pitch"):
                    st.markdown('<div class="expander-content">' + 
                              formatted_results["Create compelling pitch materials"] +
                              '</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Success message
            st.markdown('<div class="success-message">✨ Analysis completed! Review your detailed insights above.</div>', 
                       unsafe_allow_html=True)

if __name__ == "__main__":
    main()