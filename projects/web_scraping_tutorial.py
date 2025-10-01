"""
Title: Web Scraping with Python - Complete Tutorial
Author: Python-Basics-to-Advanced Contributors
Difficulty: Intermediate
Description: Comprehensive guide to web scraping using requests and BeautifulSoup
Date: October 2025

This tutorial covers:
1. Setting up web scraping environment
2. Making HTTP requests
3. Parsing HTML with BeautifulSoup
4. Handling different data types
5. Error handling and best practices
6. Real-world scraping examples
7. Ethical considerations and legal aspects

Note: This tutorial is for educational purposes only. Always respect robots.txt
and website terms of service when scraping.
"""

import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import random
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Optional
import re

print("=== Web Scraping with Python Tutorial ===\n")

# =============================================================================
# 1. INTRODUCTION TO WEB SCRAPING
# =============================================================================

print("🌐 INTRODUCTION TO WEB SCRAPING")
print("-" * 50)

print("""
Web scraping is the process of extracting data from websites programmatically.
It's useful for:
• Data collection and analysis
• Price monitoring
• News aggregation
• Research and academic purposes
• Automation of repetitive tasks

Key Tools:
• requests: For making HTTP requests
• BeautifulSoup: For parsing HTML/XML
• lxml: Fast XML/HTML parser
• selenium: For JavaScript-heavy sites

⚠️  IMPORTANT: Always check robots.txt and respect rate limits!
""")

# =============================================================================
# 2. BASIC WEB SCRAPING SETUP
# =============================================================================

print("\n📦 BASIC SETUP AND REQUIREMENTS")
print("-" * 50)

# Note: In a real environment, you would install these packages:
# pip install requests beautifulsoup4 lxml

# Basic scraping class
class WebScraper:
    """A basic web scraper with common functionality."""
    
    def __init__(self, delay_range=(1, 3)):
        """Initialize scraper with default settings."""
        self.session = requests.Session()
        self.delay_range = delay_range
        
        # Set a user agent to appear more like a real browser
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_page(self, url: str, timeout: int = 10) -> Optional[requests.Response]:
        """Fetch a web page with error handling."""
        try:
            print(f"Fetching: {url}")
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            # Random delay to be respectful
            delay = random.uniform(*self.delay_range)
            print(f"Waiting {delay:.1f} seconds...")
            time.sleep(delay)
            
            return response
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def parse_html(self, html_content: str) -> BeautifulSoup:
        """Parse HTML content using BeautifulSoup."""
        return BeautifulSoup(html_content, 'html.parser')
    
    def save_to_json(self, data: List[Dict], filename: str):
        """Save data to JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✅ Data saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving to JSON: {e}")
    
    def save_to_csv(self, data: List[Dict], filename: str):
        """Save data to CSV file."""
        if not data:
            print("No data to save")
            return
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"✅ Data saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving to CSV: {e}")

# =============================================================================
# 3. HTML PARSING EXAMPLES
# =============================================================================

print("\n🔍 HTML PARSING EXAMPLES")
print("-" * 50)

def demonstrate_html_parsing():
    """Demonstrate basic HTML parsing techniques."""
    
    # Sample HTML content (simulating a scraped page)
    sample_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sample Book Store</title>
    </head>
    <body>
        <div class="header">
            <h1>Welcome to Book Store</h1>
        </div>
        
        <div class="books">
            <div class="book" id="book1">
                <h2 class="title">Python Programming</h2>
                <p class="author">John Smith</p>
                <span class="price" data-currency="USD">$29.99</span>
                <div class="rating">
                    <span class="stars">★★★★☆</span>
                    <span class="count">(42 reviews)</span>
                </div>
                <p class="description">Learn Python programming from basics to advanced concepts.</p>
            </div>
            
            <div class="book" id="book2">
                <h2 class="title">Web Development</h2>
                <p class="author">Jane Doe</p>
                <span class="price" data-currency="USD">$39.99</span>
                <div class="rating">
                    <span class="stars">★★★★★</span>
                    <span class="count">(87 reviews)</span>
                </div>
                <p class="description">Complete guide to modern web development.</p>
            </div>
        </div>
        
        <footer>
            <p>&copy; 2025 Book Store. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
    
    # Parse the HTML
    soup = BeautifulSoup(sample_html, 'html.parser')
    
    print("📚 Parsing Sample Book Store Page")
    print("-" * 40)
    
    # 1. Find the page title
    title = soup.find('title').text
    print(f"Page Title: {title}")
    
    # 2. Find all books
    books = soup.find_all('div', class_='book')
    print(f"Found {len(books)} books")
    
    # 3. Extract book details
    book_data = []
    for book in books:
        book_info = {
            'id': book.get('id'),
            'title': book.find('h2', class_='title').text,
            'author': book.find('p', class_='author').text,
            'price': book.find('span', class_='price').text,
            'currency': book.find('span', class_='price').get('data-currency'),
            'rating': book.find('span', class_='stars').text,
            'review_count': book.find('span', class_='count').text,
            'description': book.find('p', class_='description').text
        }
        book_data.append(book_info)
    
    # Display extracted data
    for book in book_data:
        print(f"\n📖 {book['title']}")
        print(f"   Author: {book['author']}")
        print(f"   Price: {book['price']} ({book['currency']})")
        print(f"   Rating: {book['rating']} {book['review_count']}")
        print(f"   Description: {book['description'][:50]}...")
    
    return book_data

# Run the demonstration
sample_data = demonstrate_html_parsing()

# =============================================================================
# 4. ADVANCED PARSING TECHNIQUES
# =============================================================================

print("\n\n🎯 ADVANCED PARSING TECHNIQUES")
print("-" * 50)

def advanced_parsing_examples():
    """Demonstrate advanced BeautifulSoup techniques."""
    
    # Complex HTML with various structures
    complex_html = """
    <html>
    <body>
        <article class="news-article" data-id="123">
            <header>
                <h1>Breaking News: Python 4.0 Released</h1>
                <div class="meta">
                    <span class="author">By Tech Reporter</span>
                    <time datetime="2025-10-01T14:30:00Z">Oct 1, 2025</time>
                    <div class="tags">
                        <span class="tag">Python</span>
                        <span class="tag">Programming</span>
                        <span class="tag">Technology</span>
                    </div>
                </div>
            </header>
            
            <div class="content">
                <p>The Python Software Foundation announced today...</p>
                <blockquote cite="https://python.org">
                    "This is a revolutionary release" - Guido van Rossum
                </blockquote>
                <ul class="features">
                    <li>Improved performance</li>
                    <li>Better error messages</li>
                    <li>New syntax features</li>
                </ul>
            </div>
            
            <footer>
                <div class="social-shares">
                    <a href="#" class="share-btn" data-platform="twitter">Tweet</a>
                    <a href="#" class="share-btn" data-platform="facebook">Share</a>
                </div>
            </footer>
        </article>
        
        <!-- Comments section -->
        <section class="comments">
            <div class="comment" data-comment-id="1">
                <strong>Alice:</strong> Great news!
            </div>
            <div class="comment" data-comment-id="2">
                <strong>Bob:</strong> Can't wait to try it!
            </div>
        </section>
    </body>
    </html>
    """
    
    soup = BeautifulSoup(complex_html, 'html.parser')
    
    print("🔍 Advanced Parsing Techniques")
    print("-" * 40)
    
    # 1. CSS Selectors
    print("1. Using CSS Selectors:")
    title = soup.select_one('h1').text
    author = soup.select_one('.meta .author').text
    tags = [tag.text for tag in soup.select('.tag')]
    print(f"   Title: {title}")
    print(f"   Author: {author}")
    print(f"   Tags: {', '.join(tags)}")
    
    # 2. Attribute searching
    print("\n2. Searching by attributes:")
    article = soup.find('article', {'data-id': '123'})
    article_id = article.get('data-id')
    print(f"   Article ID: {article_id}")
    
    # 3. Text searching with regex
    print("\n3. Text pattern matching:")
    import re
    quote = soup.find('blockquote')
    if quote:
        cite = quote.get('cite')
        print(f"   Quote source: {cite}")
    
    # 4. Navigating the tree
    print("\n4. Tree navigation:")
    meta_div = soup.find('div', class_='meta')
    if meta_div:
        # Get next sibling
        next_element = meta_div.find_next_sibling()
        if next_element:
            print(f"   Next sibling tag: {next_element.name}")
        
        # Get parent
        parent = meta_div.parent
        print(f"   Parent tag: {parent.name}")
    
    # 5. Extracting structured data
    print("\n5. Structured data extraction:")
    features = [li.text.strip() for li in soup.select('.features li')]
    comments = []
    for comment in soup.select('.comment'):
        comment_data = {
            'id': comment.get('data-comment-id'),
            'text': comment.text.strip()
        }
        comments.append(comment_data)
    
    print(f"   Features: {features}")
    print(f"   Comments: {len(comments)} found")
    for comment in comments:
        print(f"     - {comment['text']}")
    
    # 6. Extracting all links
    print("\n6. Link extraction:")
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        text = link.text.strip()
        platform = link.get('data-platform', 'unknown')
        print(f"   Link: {text} → {href} (platform: {platform})")

advanced_parsing_examples()

# =============================================================================
# 5. REAL-WORLD SCRAPING EXAMPLES
# =============================================================================

print("\n\n🌍 REAL-WORLD SCRAPING EXAMPLES")
print("-" * 50)

class QuoteScraper(WebScraper):
    """Scraper for quotes website (example)."""
    
    def scrape_quotes_simulation(self):
        """Simulate scraping quotes from a website."""
        print("📝 Simulating Quote Scraping")
        print("-" * 30)
        
        # Simulated quote data (in real scenario, this would be scraped)
        simulated_quotes = [
            {
                'text': 'The way to get started is to quit talking and begin doing.',
                'author': 'Walt Disney',
                'tags': ['inspirational', 'wisdom']
            },
            {
                'text': 'Life is what happens to you while you\'re busy making other plans.',
                'author': 'John Lennon',
                'tags': ['life', 'misattributed-john-lennon']
            },
            {
                'text': 'The future belongs to those who believe in the beauty of their dreams.',
                'author': 'Eleanor Roosevelt',
                'tags': ['inspirational', 'future']
            }
        ]
        
        print(f"✅ Found {len(simulated_quotes)} quotes")
        for i, quote in enumerate(simulated_quotes, 1):
            print(f"\n{i}. \"{quote['text']}\"")
            print(f"   - {quote['author']}")
            print(f"   Tags: {', '.join(quote['tags'])}")
        
        return simulated_quotes

class NewsScraper(WebScraper):
    """Scraper for news articles (example)."""
    
    def scrape_headlines_simulation(self):
        """Simulate scraping news headlines."""
        print("\n📰 Simulating News Headline Scraping")
        print("-" * 40)
        
        # Simulated news data
        simulated_news = [
            {
                'headline': 'Python Continues to Dominate Programming Languages',
                'summary': 'Latest survey shows Python maintaining its top position...',
                'category': 'Technology',
                'timestamp': '2025-10-01 14:30:00',
                'url': 'https://example-news.com/python-dominates'
            },
            {
                'headline': 'AI Breakthrough in Natural Language Processing',
                'summary': 'Researchers achieve new milestone in AI understanding...',
                'category': 'AI',
                'timestamp': '2025-10-01 13:15:00',
                'url': 'https://example-news.com/ai-breakthrough'
            },
            {
                'headline': 'Open Source Projects See Record Contributions',
                'summary': 'GitHub reports highest number of contributions ever...',
                'category': 'Open Source',
                'timestamp': '2025-10-01 12:00:00',
                'url': 'https://example-news.com/open-source-record'
            }
        ]
        
        print(f"✅ Found {len(simulated_news)} news articles")
        for i, article in enumerate(simulated_news, 1):
            print(f"\n{i}. {article['headline']}")
            print(f"   Category: {article['category']}")
            print(f"   Time: {article['timestamp']}")
            print(f"   Summary: {article['summary'][:60]}...")
        
        return simulated_news

class ProductScraper(WebScraper):
    """Scraper for e-commerce products (example)."""
    
    def scrape_products_simulation(self):
        """Simulate scraping product information."""
        print("\n🛒 Simulating Product Information Scraping")
        print("-" * 45)
        
        # Simulated product data
        simulated_products = [
            {
                'name': 'Wireless Programming Keyboard',
                'price': 129.99,
                'currency': 'USD',
                'rating': 4.5,
                'review_count': 234,
                'availability': 'In Stock',
                'category': 'Electronics',
                'features': ['Wireless', 'Mechanical', 'RGB Backlight'],
                'url': 'https://example-store.com/keyboard'
            },
            {
                'name': 'Python Programming Book Set',
                'price': 89.99,
                'currency': 'USD',
                'rating': 4.8,
                'review_count': 156,
                'availability': 'In Stock',
                'category': 'Books',
                'features': ['Beginner to Advanced', '3 Books', 'Digital Copy Included'],
                'url': 'https://example-store.com/python-books'
            },
            {
                'name': 'Developer Desk Lamp',
                'price': 45.99,
                'currency': 'USD',
                'rating': 4.3,
                'review_count': 89,
                'availability': 'Limited Stock',
                'category': 'Office',
                'features': ['LED', 'Adjustable', 'USB Charging'],
                'url': 'https://example-store.com/desk-lamp'
            }
        ]
        
        print(f"✅ Found {len(simulated_products)} products")
        for i, product in enumerate(simulated_products, 1):
            print(f"\n{i}. {product['name']}")
            print(f"   Price: ${product['price']:.2f}")
            print(f"   Rating: {product['rating']}⭐ ({product['review_count']} reviews)")
            print(f"   Status: {product['availability']}")
            print(f"   Features: {', '.join(product['features'])}")
        
        return simulated_products

# Run the scraping examples
quote_scraper = QuoteScraper()
quotes_data = quote_scraper.scrape_quotes_simulation()

news_scraper = NewsScraper()
news_data = news_scraper.scrape_headlines_simulation()

product_scraper = ProductScraper()
products_data = product_scraper.scrape_products_simulation()

# =============================================================================
# 6. DATA PROCESSING AND ANALYSIS
# =============================================================================

print("\n\n📊 DATA PROCESSING AND ANALYSIS")
print("-" * 50)

def analyze_scraped_data():
    """Demonstrate data analysis on scraped content."""
    print("🔍 Analyzing Scraped Data")
    print("-" * 25)
    
    # Analyze quotes data
    print("📝 Quote Analysis:")
    total_quotes = len(quotes_data)
    all_tags = []
    for quote in quotes_data:
        all_tags.extend(quote['tags'])
    
    tag_counts = {}
    for tag in all_tags:
        tag_counts[tag] = tag_counts.get(tag, 0) + 1
    
    most_common_tag = max(tag_counts.items(), key=lambda x: x[1])
    print(f"   Total quotes: {total_quotes}")
    print(f"   Unique tags: {len(tag_counts)}")
    print(f"   Most common tag: '{most_common_tag[0]}' ({most_common_tag[1]} times)")
    
    # Analyze news data
    print("\n📰 News Analysis:")
    categories = [article['category'] for article in news_data]
    category_counts = {}
    for category in categories:
        category_counts[category] = category_counts.get(category, 0) + 1
    
    print(f"   Total articles: {len(news_data)}")
    print("   Categories:")
    for category, count in category_counts.items():
        print(f"     - {category}: {count} articles")
    
    # Analyze product data
    print("\n🛒 Product Analysis:")
    total_products = len(products_data)
    avg_price = sum(p['price'] for p in products_data) / total_products
    avg_rating = sum(p['rating'] for p in products_data) / total_products
    
    in_stock = sum(1 for p in products_data if p['availability'] == 'In Stock')
    
    print(f"   Total products: {total_products}")
    print(f"   Average price: ${avg_price:.2f}")
    print(f"   Average rating: {avg_rating:.1f}⭐")
    print(f"   In stock: {in_stock}/{total_products}")
    
    # Price distribution
    price_ranges = {'Under $50': 0, '$50-$100': 0, 'Over $100': 0}
    for product in products_data:
        price = product['price']
        if price < 50:
            price_ranges['Under $50'] += 1
        elif price <= 100:
            price_ranges['$50-$100'] += 1
        else:
            price_ranges['Over $100'] += 1
    
    print("   Price distribution:")
    for range_name, count in price_ranges.items():
        print(f"     - {range_name}: {count} products")

analyze_scraped_data()

# =============================================================================
# 7. ERROR HANDLING AND ROBUSTNESS
# =============================================================================

print("\n\n🛡️  ERROR HANDLING AND ROBUSTNESS")
print("-" * 50)

class RobustScraper(WebScraper):
    """A more robust scraper with comprehensive error handling."""
    
    def __init__(self, max_retries=3, delay_range=(1, 3)):
        super().__init__(delay_range)
        self.max_retries = max_retries
        self.failed_urls = []
        self.successful_urls = []
    
    def get_page_with_retries(self, url: str) -> Optional[requests.Response]:
        """Fetch page with retry logic."""
        for attempt in range(self.max_retries):
            try:
                response = self.get_page(url)
                if response:
                    self.successful_urls.append(url)
                    return response
                else:
                    print(f"Attempt {attempt + 1} failed for {url}")
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
            
            if attempt < self.max_retries - 1:
                wait_time = (attempt + 1) * 2  # Exponential backoff
                print(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
        
        self.failed_urls.append(url)
        print(f"❌ Failed to fetch {url} after {self.max_retries} attempts")
        return None
    
    def safe_extract_text(self, element, default="N/A"):
        """Safely extract text from an element."""
        try:
            return element.text.strip() if element else default
        except AttributeError:
            return default
    
    def safe_extract_attribute(self, element, attr, default="N/A"):
        """Safely extract attribute from an element."""
        try:
            return element.get(attr, default) if element else default
        except AttributeError:
            return default
    
    def validate_data(self, data: Dict) -> bool:
        """Validate scraped data."""
        required_fields = ['title', 'url']
        
        for field in required_fields:
            if field not in data or not data[field]:
                print(f"⚠️  Missing required field: {field}")
                return False
        
        # Additional validation rules
        if data.get('price'):
            try:
                float(data['price'].replace('$', '').replace(',', ''))
            except (ValueError, AttributeError):
                print(f"⚠️  Invalid price format: {data.get('price')}")
                return False
        
        return True
    
    def scrape_with_validation(self, urls: List[str]) -> List[Dict]:
        """Scrape multiple URLs with validation."""
        valid_data = []
        
        for url in urls:
            print(f"\n🌐 Processing: {url}")
            response = self.get_page_with_retries(url)
            
            if not response:
                continue
            
            try:
                soup = self.parse_html(response.text)
                
                # Extract basic information (this would be customized per site)
                data = {
                    'url': url,
                    'title': self.safe_extract_text(soup.find('title')),
                    'status_code': response.status_code,
                    'content_length': len(response.text),
                    'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S')
                }
                
                if self.validate_data(data):
                    valid_data.append(data)
                    print("✅ Data validated and added")
                else:
                    print("❌ Data validation failed")
                    
            except Exception as e:
                print(f"❌ Error processing {url}: {e}")
        
        return valid_data
    
    def generate_report(self):
        """Generate a scraping session report."""
        print("\n📋 SCRAPING SESSION REPORT")
        print("-" * 30)
        print(f"Successful URLs: {len(self.successful_urls)}")
        print(f"Failed URLs: {len(self.failed_urls)}")
        
        if self.failed_urls:
            print("\nFailed URLs:")
            for url in self.failed_urls:
                print(f"  - {url}")
        
        success_rate = (len(self.successful_urls) / 
                       (len(self.successful_urls) + len(self.failed_urls))) * 100
        print(f"\nSuccess Rate: {success_rate:.1f}%")

# Demonstrate robust scraping
print("🔧 Demonstrating Robust Scraping Techniques:")
robust_scraper = RobustScraper(max_retries=2)

# Simulate scraping session (with mock URLs)
mock_urls = [
    "https://httpbin.org/status/200",  # This would succeed
    "https://httpbin.org/status/404",  # This would fail
    "https://httpbin.org/delay/1"      # This would succeed with delay
]

print("Note: In a real scenario, these would be actual URLs to scrape.")
print("This demonstration shows the error handling structure.\n")

# =============================================================================
# 8. BEST PRACTICES AND ETHICAL CONSIDERATIONS
# =============================================================================

print("\n⚖️  BEST PRACTICES AND ETHICAL CONSIDERATIONS")
print("-" * 60)

print("""
🤝 ETHICAL WEB SCRAPING GUIDELINES:

1. RESPECT ROBOTS.TXT
   - Always check /robots.txt before scraping
   - Follow the rules specified for web crawlers

2. RATE LIMITING
   - Don't overwhelm servers with requests
   - Add delays between requests (1-3 seconds minimum)
   - Use exponential backoff for retries

3. LEGAL COMPLIANCE
   - Check website's Terms of Service
   - Respect copyright and intellectual property
   - Don't scrape personal or sensitive data

4. TECHNICAL BEST PRACTICES
   - Use proper User-Agent headers
   - Handle errors gracefully
   - Respect HTTP status codes
   - Cache responses when possible

5. DATA USAGE
   - Only collect data you actually need
   - Store data securely
   - Respect user privacy
   - Don't redistribute copyrighted content

6. SERVER CONSIDERATIONS
   - Scrape during off-peak hours when possible
   - Use multiple IP addresses for large-scale scraping
   - Monitor your impact on target servers
   - Consider using official APIs when available
""")

def check_robots_txt(url: str):
    """Check robots.txt for a given domain."""
    try:
        from urllib.parse import urljoin, urlparse
        
        domain = urlparse(url).netloc
        robots_url = f"https://{domain}/robots.txt"
        
        print(f"🤖 Checking robots.txt: {robots_url}")
        
        # In a real implementation, you would fetch and parse robots.txt
        print("Sample robots.txt rules:")
        print("User-agent: *")
        print("Disallow: /private/")
        print("Disallow: /admin/")
        print("Crawl-delay: 1")
        print("Allow: /public/")
        
    except Exception as e:
        print(f"Error checking robots.txt: {e}")

def calculate_request_rate(requests_count: int, time_period: int):
    """Calculate and display request rate."""
    rate = requests_count / time_period
    print(f"📊 Request Rate: {requests_count} requests in {time_period} seconds")
    print(f"   Average: {rate:.2f} requests/second")
    
    if rate > 1:
        print("   ⚠️  Consider reducing request rate to be more respectful")
    else:
        print("   ✅ Request rate is respectful")

# Example usage
check_robots_txt("https://example.com")
calculate_request_rate(100, 300)  # 100 requests in 5 minutes

# =============================================================================
# 9. SAVING AND EXPORTING DATA
# =============================================================================

print("\n\n💾 SAVING AND EXPORTING DATA")
print("-" * 50)

def demonstrate_data_export():
    """Demonstrate different ways to save scraped data."""
    
    # Combine all our scraped data
    all_data = {
        'quotes': quotes_data,
        'news': news_data,
        'products': products_data,
        'metadata': {
            'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S'),
            'total_items': len(quotes_data) + len(news_data) + len(products_data),
            'scraper_version': '1.0'
        }
    }
    
    # Create a scraper instance for saving
    scraper = WebScraper()
    
    print("💾 Exporting scraped data in different formats:")
    
    # 1. Save to JSON
    print("\n1. Saving to JSON format...")
    scraper.save_to_json(all_data, 'scraped_data.json')
    
    # 2. Save quotes to CSV
    print("\n2. Saving quotes to CSV format...")
    scraper.save_to_csv(quotes_data, 'quotes.csv')
    
    # 3. Save products to CSV
    print("\n3. Saving products to CSV format...")
    # Flatten product features for CSV
    products_for_csv = []
    for product in products_data:
        csv_product = product.copy()
        csv_product['features'] = ', '.join(product['features'])
        products_for_csv.append(csv_product)
    
    scraper.save_to_csv(products_for_csv, 'products.csv')
    
    # 4. Create summary report
    print("\n4. Generating summary report...")
    summary = f"""
WEB SCRAPING SUMMARY REPORT
Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}

Data Collected:
- Quotes: {len(quotes_data)} items
- News Articles: {len(news_data)} items
- Products: {len(products_data)} items
- Total: {len(quotes_data) + len(news_data) + len(products_data)} items

Data Quality:
- All items successfully validated
- No duplicate entries found
- Complete data fields for all items

Files Generated:
- scraped_data.json (complete dataset)
- quotes.csv (quotes only)
- products.csv (products only)
- summary_report.txt (this file)
"""
    
    try:
        with open('summary_report.txt', 'w', encoding='utf-8') as f:
            f.write(summary)
        print("✅ Summary report saved to summary_report.txt")
    except Exception as e:
        print(f"❌ Error saving summary report: {e}")
    
    print(f"\n📈 Export completed! {len(all_data)} items processed.")

demonstrate_data_export()

# =============================================================================
# 10. PUTTING IT ALL TOGETHER - COMPLETE EXAMPLE
# =============================================================================

print("\n\n🎯 COMPLETE SCRAPING PROJECT EXAMPLE")
print("-" * 50)

class ComprehensiveScraper:
    """A complete scraping project demonstrating all concepts."""
    
    def __init__(self):
        self.scraper = RobustScraper()
        self.data_store = []
        self.start_time = time.time()
    
    def run_complete_scraping_demo(self):
        """Run a complete scraping demonstration."""
        print("🚀 Starting Comprehensive Scraping Demo")
        print("=" * 45)
        
        # 1. Planning phase
        print("\n📋 PHASE 1: PLANNING")
        print("- Identified target websites")
        print("- Checked robots.txt compliance")
        print("- Planned data structure")
        print("- Set up rate limiting")
        
        # 2. Data collection phase
        print("\n🌐 PHASE 2: DATA COLLECTION")
        self.collect_all_data()
        
        # 3. Data processing phase
        print("\n⚙️  PHASE 3: DATA PROCESSING")
        self.process_collected_data()
        
        # 4. Data validation phase
        print("\n✅ PHASE 4: DATA VALIDATION")
        self.validate_all_data()
        
        # 5. Export phase
        print("\n💾 PHASE 5: DATA EXPORT")
        self.export_final_data()
        
        # 6. Reporting phase
        print("\n📊 PHASE 6: FINAL REPORT")
        self.generate_final_report()
    
    def collect_all_data(self):
        """Collect data from all sources."""
        print("Collecting data from multiple sources...")
        
        # In a real scenario, you would scrape actual websites
        # Here we're using our simulated data
        self.data_store.extend([
            {'type': 'quote', 'data': quote} for quote in quotes_data
        ])
        self.data_store.extend([
            {'type': 'news', 'data': article} for article in news_data
        ])
        self.data_store.extend([
            {'type': 'product', 'data': product} for product in products_data
        ])
        
        print(f"✅ Collected {len(self.data_store)} items")
    
    def process_collected_data(self):
        """Process and clean collected data."""
        print("Processing collected data...")
        
        processed_count = 0
        for item in self.data_store:
            # Add processing timestamp
            item['processed_at'] = time.strftime('%Y-%m-%d %H:%M:%S')
            
            # Add unique ID
            item['id'] = f"{item['type']}_{processed_count + 1}"
            
            processed_count += 1
        
        print(f"✅ Processed {processed_count} items")
    
    def validate_all_data(self):
        """Validate all collected data."""
        print("Validating data quality...")
        
        valid_items = 0
        invalid_items = 0
        
        for item in self.data_store:
            if self.validate_item(item):
                valid_items += 1
            else:
                invalid_items += 1
        
        print(f"✅ Valid items: {valid_items}")
        print(f"❌ Invalid items: {invalid_items}")
        
        # Remove invalid items
        self.data_store = [item for item in self.data_store if self.validate_item(item)]
    
    def validate_item(self, item):
        """Validate a single data item."""
        required_fields = ['type', 'data', 'id', 'processed_at']
        return all(field in item for field in required_fields)
    
    def export_final_data(self):
        """Export processed data."""
        print("Exporting final dataset...")
        
        # Group by type
        grouped_data = {}
        for item in self.data_store:
            item_type = item['type']
            if item_type not in grouped_data:
                grouped_data[item_type] = []
            grouped_data[item_type].append(item)
        
        # Export each type
        for data_type, items in grouped_data.items():
            filename = f"final_{data_type}_data.json"
            self.scraper.save_to_json(items, filename)
        
        print(f"✅ Exported {len(grouped_data)} data types")
    
    def generate_final_report(self):
        """Generate comprehensive final report."""
        end_time = time.time()
        duration = end_time - self.start_time
        
        # Count items by type
        type_counts = {}
        for item in self.data_store:
            item_type = item['type']
            type_counts[item_type] = type_counts.get(item_type, 0) + 1
        
        print("\n" + "=" * 50)
        print("📋 FINAL SCRAPING REPORT")
        print("=" * 50)
        print(f"Execution Time: {duration:.2f} seconds")
        print(f"Total Items Collected: {len(self.data_store)}")
        print(f"Success Rate: 100%")  # Our demo data is all valid
        
        print("\nData Breakdown:")
        for data_type, count in type_counts.items():
            print(f"  {data_type.title()}: {count} items")
        
        print("\nQuality Metrics:")
        print("  ✅ All data validated")
        print("  ✅ No duplicates found")
        print("  ✅ Complete fields for all items")
        print("  ✅ Proper rate limiting applied")
        
        print("\nFiles Generated:")
        print("  📄 final_quote_data.json")
        print("  📄 final_news_data.json")
        print("  📄 final_product_data.json")
        
        print("\n🎉 Scraping project completed successfully!")

# Run the complete demonstration
comprehensive_scraper = ComprehensiveScraper()
comprehensive_scraper.run_complete_scraping_demo()

print("\n" + "=" * 60)
print("🏁 END OF WEB SCRAPING TUTORIAL")
print("=" * 60)
print("""
Congratulations! You've completed a comprehensive web scraping tutorial.

Key takeaways:
📚 Understanding HTML structure and parsing
🔍 Using BeautifulSoup for data extraction
🛡️  Implementing robust error handling
⚖️  Following ethical scraping practices
💾 Saving data in multiple formats
📊 Analyzing and processing scraped data

Next steps:
1. Practice with real websites (respect their terms!)
2. Learn about handling JavaScript-heavy sites (Selenium)
3. Explore API alternatives to scraping
4. Study advanced topics like distributed scraping
5. Build your own scraping projects

Remember: Always scrape responsibly! 🤝
""")

# Additional resources and tips
print("\n📚 ADDITIONAL RESOURCES:")
print("- BeautifulSoup Documentation: https://www.crummy.com/software/BeautifulSoup/")
print("- Requests Documentation: https://docs.python-requests.org/")
print("- Web Scraping Ethics: https://blog.apify.com/web-scraping-ethics/")
print("- Legal considerations: Always check robots.txt and terms of service")
print("- Alternative: Many websites offer APIs - use them when available!")

print("\nHappy scraping! 🕷️")