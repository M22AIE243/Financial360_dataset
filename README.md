# Financial360 Dataset

**Pairing real-world financial data with visualizations (charts/graphs) and their summaries for over 340 companies.**

## Introduction

To support AI research in the financial domain, we introduce **Financial360**—a carefully curated, domain-specific, multi-modal dataset. This dataset is purpose-built for training and evaluating image summarization models, especially lightweight vision architectures that need to make sense of financial information at a glance.

Financial360 brings together real-world market behavior from over 340 publicly traded companies, covering data from **2023 to 2025**, all collected via the Yahoo Finance API.


Although the dataset was created using real financial data, the visualizations and summaries are synthetically generated—ensuring clarity, consistency, and scalability without relying on scraped or human-written reports.

It’s designed not just for researchers in vision and language tasks, but also for those looking to validate or fine-tune small, efficient models on domain-specific data with real-world utility.

## Dataset Structure (Company-wise Example: Apple - AAPL)

AAPL/
├── AAPL_stock_price.png                 # Line graph of stock prices
├── AAPL_stock_price_summary.txt         # Summary of the line graph
│
├── AAPL_stock_price_with_caption.png    # Same line graph with caption included in image
├── AAPL_stock_price_with_caption_summary.txt # Summary for the captioned chart
│
├── AAPL_volume_bar.png                   # Bar chart for trading volume
├── AAPL_volume_bar_summary.txt           # Summary for volume bar chart
│
├── AAPL_volume_pie.png                   # Pie chart showing quarterly distribution
├── AAPL_volume_pie_summary.txt           # Summary for pie chart
│
├── AAPL_summary.txt                     # General company-level summary
├── AAPL_summary_updated.txt             # Enhanced or corrected version of the summary
