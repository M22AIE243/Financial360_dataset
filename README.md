# Financial360_dataset
Pairing real-world financial data with visualizations(chart/Graph) and its summaries  for over 340 companies,


To support AI research in the financial domain, Iintroduced Financial360—a carefully curated, domain-specific, multi-modal dataset. This dataset is purpose-built for training and evaluating image summarization models, especially lightweight vision architectures that need to make sense of financial information at a glance.

Financial360 brings together real-world market behavior from over 340 publicly traded companies, covering data from 2023 
to 2025, all collected via the Yahoo Finance API. 


Each company’s profile in the dataset includes:

Structured textual insights extracted from time series data, summarizing key metrics like total trading days, average prices, and volume trends.

Programmatically generated charts such as stock price line graphs, bar charts for trading volume, and pie charts showing quarterly distribution—designed to help vision models learn from realistic financial visuals.

Every chart/Graphs in the dataset is paired with a machine-written summary, giving researchers a consistent way to test how accurately models can interpret financial visuals.

Although the dataset was created using in real financial data, the visualizations and summaries are synthetically generated—ensuring clarity, consistency, and scalability without relying on scraped or human-written reports. 

It’s designed not just for researchers in vision and language tasks, but also for those looking to validate or fine-tune small, efficient models on domain-specific data with real-world utility

#Dataset Structure company wise (Exaple Apple)
AAPL/
│
├── AAPL_stock_price.png                   # Line graph of stock prices
├── AAPL_stock_price_summary.txt           # Summary of the line graph
│
├── AAPL_stock_price_with_caption.png      # Same line graph with caption included in image
├── AAPL_stock_price_with_caption_summary.txt  # Summary for the captioned chart
│
├── AAPL_volume_bar.png                    # Bar chart for trading volume
├── AAPL_volume_bar_summary.txt            # Summary for volume bar chart
│
├── AAPL_volume_pie.png                    # Pie chart showing quarterly distribution
├── AAPL_volume_pie_summary.txt            # Summary for pie chart
│
├── AAPL_summary.txt                       # General company-level summary
├── AAPL_summary_updated.txt               # Enhanced or corrected version of the summary




#-----for running python files------------
To run any python File 

Export GROQ_API_KEY="your key in double Quotes from groq"

Also verify the folder location from where code is reading/writing files.


Based on imports you may need to run pip install commands.


Thank you.
