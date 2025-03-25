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

    st.title("🚀 ThinkTank AI - Startup Idea Analyzer")
    st.markdown("""
    Input your startup idea below and our AI agents will analyze various aspects of your business concept.
    Get comprehensive insights on market research, feasibility, customer analysis, and more!
    """)

    # Input section
    startup_idea = st.text_area(
        "Enter your startup idea",
        height=150,
        placeholder="Describe your startup idea in detail..."
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

            # Display results in organized sections
            with col1:
                # Market and Customer Analysis Section
                st.subheader("📊 Market & Customer Analysis")
                with st.expander("Market Analysis", expanded=True):
                    if "Analyze market size, trends, and competitor landscape" in formatted_results:
                        st.markdown(formatted_results["Analyze market size, trends, and competitor landscape"])
                
                with st.expander("Customer Analysis", expanded=True):
                    if "Define target customers and their needs" in formatted_results:
                        st.markdown(formatted_results["Define target customers and their needs"])
                
                # Business Strategy Section
                st.subheader("💼 Business Strategy")
                with st.expander("Business Model", expanded=True):
                    if "Design comprehensive business model" in formatted_results:
                        st.markdown(formatted_results["Design comprehensive business model"])
                
                with st.expander("Competitive Analysis", expanded=True):
                    if "Identify key differentiators and advantages" in formatted_results:
                        st.markdown(formatted_results["Identify key differentiators and advantages"])

            with col2:
                # Technical & Financial Analysis Section
                st.subheader("🔧 Technical & Financial Analysis")
                with st.expander("Feasibility Analysis", expanded=True):
                    if "Evaluate technical and financial feasibility" in formatted_results:
                        st.markdown(formatted_results["Evaluate technical and financial feasibility"])
                
                with st.expander("Technology Stack", expanded=True):
                    if "Recommend optimal technology stack" in formatted_results:
                        st.markdown(formatted_results["Recommend optimal technology stack"])
                
                # Go-to-Market Section
                st.subheader("🎯 Go-to-Market Strategy")
                with st.expander("Monetization Strategy", expanded=True):
                    if "Develop revenue generation strategies" in formatted_results:
                        st.markdown(formatted_results["Develop revenue generation strategies"])
                
                with st.expander("Go-to-Market Strategy", expanded=True):
                    if "Create launch and market entry strategy" in formatted_results:
                        st.markdown(formatted_results["Create launch and market entry strategy"])

            # Investment Summary Section
            st.subheader("💰 Investment Summary")
            with st.expander("Investor Pitch", expanded=True):
                if "Create compelling pitch materials" in formatted_results:
                    st.markdown(formatted_results["Create compelling pitch materials"])

            st.success("Analysis completed! Review the detailed insights above.")

if __name__ == "__main__":
    main()