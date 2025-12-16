# LangChain Community Tools Documentation

This document provides a comprehensive overview of all available tools in the LangChain Community package, including usage explanations and examples.

---

## Table of Contents

1. [Core Tools](#core-tools)
2. [Search Tools](#search-tools)
3. [AI Network Tools](#ai-network-tools)
4. [Azure AI Services](#azure-ai-services)
5. [File Management Tools](#file-management-tools)
6. [Communication Tools](#communication-tools)
7. [Database Tools](#database-tools)
8. [Financial Tools](#financial-tools)
9. [Web & Browser Tools](#web--browser-tools)
10. [AI/ML Tools](#aiml-tools)
11. [Productivity Tools](#productivity-tools)
12. [Knowledge & Research Tools](#knowledge--research-tools)
13. [Integration Tools](#integration-tools)
14. [Recommended Tools for Your Chatbot](#recommended-tools-for-your-chatbot)

---

## Core Tools

### BaseTool
**Usage:** Base class for creating custom tools in LangChain. Inherit from this to build your own tool implementations.

**Example:** Create a custom tool that extends BaseTool to add domain-specific functionality like weather queries or API integrations.

### Tool
**Usage:** Simple tool wrapper for functions that don't require structured input/output. Use this for basic function-to-tool conversions.

**Example:** Convert a Python function like `def greet(name): return f"Hello {name}"` into a LangChain tool that can be used by agents.

### StructuredTool
**Usage:** Tool wrapper that enforces structured input/output using Pydantic models. Perfect for tools requiring validated parameters.

**Example:** Create a tool with strict typing like a calculator that requires two floats and an operation string, ensuring type safety.

### tool (decorator)
**Usage:** Decorator to convert Python functions into LangChain tools automatically. Simplifies tool creation with minimal code.

**Example:** Add `@tool` decorator above a function to make it instantly available to LangChain agents without manual configuration.

---

## Search Tools

### DuckDuckGoSearchRun
**Usage:** Performs web searches using DuckDuckGo search engine. Returns search results as text. Already integrated in your chatbot.

**Example:** User asks "What is the weather in New York?" and the tool searches DuckDuckGo to find current weather information.

### DuckDuckGoSearchResults
**Usage:** Similar to DuckDuckGoSearchRun but returns structured search results with titles, snippets, and URLs.

**Example:** Returns formatted results like `[{"title": "...", "snippet": "...", "url": "..."}]` for better result parsing.

### BingSearchRun
**Usage:** Performs web searches using Microsoft Bing search API. Requires Bing API key for authentication.

**Example:** Search for "latest AI developments" and get comprehensive results from Bing's search index.

### BingSearchResults
**Usage:** Returns structured Bing search results with metadata including relevance scores and publication dates.

**Example:** Get ranked search results with additional context like date published and domain information.

### GoogleSearchRun
**Usage:** Executes searches using Google Custom Search API. Requires Google API key and search engine ID.

**Example:** Search for "Python tutorials" and retrieve results from Google's vast search index.

### GoogleSearchResults
**Usage:** Returns structured Google search results with rich metadata including images, videos, and knowledge graph data.

**Example:** Get comprehensive search results including featured snippets, related questions, and multimedia content.

### GoogleSerperRun
**Usage:** Uses Serper.dev API for Google search results. Faster and more cost-effective than direct Google API.

**Example:** Search for "best restaurants near me" and get instant results with location-based information.

### GoogleSerperResults
**Usage:** Returns structured results from Serper.dev with enhanced metadata and faster response times.

**Example:** Get search results with additional context like ratings, prices, and business hours for local searches.

### BraveSearch
**Usage:** Performs searches using Brave Search API. Privacy-focused search engine alternative.

**Example:** Search for "cryptocurrency news" and get results from Brave's independent search index.

### TavilySearchResults
**Usage:** AI-powered search tool that returns relevant results optimized for LLM consumption. Great for RAG applications.

**Example:** Search for "quantum computing breakthroughs" and get results specifically formatted for AI understanding.

### TavilyAnswer
**Usage:** Returns direct answers to queries using Tavily's AI search, perfect for factual questions.

**Example:** Ask "What is the capital of France?" and get a direct answer instead of search result links.

### JinaSearch
**Usage:** Neural search tool that understands semantic meaning of queries, not just keywords.

**Example:** Search for "ways to save money" and get results about budgeting, investing, and financial planning even if those exact words aren't in the results.

### SearxSearchResults
**Usage:** Meta-search engine that aggregates results from multiple search engines. Privacy-focused and customizable.

**Example:** Search across Google, Bing, and DuckDuckGo simultaneously to get comprehensive results.

### SearxSearchRun
**Usage:** Executes searches using self-hosted or public Searx instances for aggregated search results.

**Example:** Get combined results from multiple search engines in a single query for better coverage.

### MojeekSearch
**Usage:** Alternative search engine that provides independent search results without tracking.

**Example:** Search for information while maintaining privacy, as Mojeek doesn't track user behavior.

### SearchAPIRun
**Usage:** Unified search API that aggregates results from multiple search engines and sources.

**Example:** Get comprehensive search results from various sources in a single API call.

### SearchAPIResults
**Usage:** Returns structured results from SearchAPI with metadata from multiple search engines.

**Example:** Receive formatted results with source attribution and relevance scores from various search providers.

### MetaphorSearchResults
**Usage:** AI-powered search that finds content based on meaning and context, not just keywords.

**Example:** Search for "articles about sustainable energy" and get semantically related content even if those exact words aren't used.

### YouSearchTool
**Usage:** Search tool using You.com's AI-powered search engine with conversational results.

**Example:** Get natural language search results that read like answers rather than just links.

---

## AI Network Tools

### AINAppOps
**Usage:** Manages applications on the AI Network blockchain. Create, update, and manage AI applications.

**Example:** Deploy a new AI model or service on the AI Network blockchain platform.

### AINOwnerOps
**Usage:** Handles ownership operations for AI Network resources. Transfer ownership, manage permissions.

**Example:** Transfer ownership of an AI Network application to another user or organization.

### AINRuleOps
**Usage:** Manages rules and policies for AI Network applications. Set up governance and access controls.

**Example:** Configure rules that determine who can access or modify an AI Network application.

### AINTransfer
**Usage:** Transfers tokens or resources within the AI Network ecosystem.

**Example:** Transfer AI Network tokens between accounts or applications.

### AINValueOps
**Usage:** Manages value operations like deposits, withdrawals, and balance queries on AI Network.

**Example:** Check balance or transfer value between AI Network accounts.

---

## Azure AI Services

### AzureAiServicesDocumentIntelligenceTool
**Usage:** Extracts text, tables, and structure from documents using Azure Document Intelligence. Perfect for PDF processing.

**Example:** Extract all text and tables from a PDF invoice to analyze billing information automatically.

### AzureAiServicesImageAnalysisTool
**Usage:** Analyzes images to detect objects, faces, text, and generate descriptions using Azure Computer Vision.

**Example:** Analyze a photo to identify objects, read text in images, and generate captions automatically.

### AzureAiServicesSpeechToTextTool
**Usage:** Converts spoken audio to text using Azure Speech Services. Supports multiple languages.

**Example:** Transcribe a voice recording or live audio stream into written text for processing.

### AzureAiServicesTextToSpeechTool
**Usage:** Converts text to natural-sounding speech using Azure Neural Voices. Multiple voice options available.

**Example:** Generate audio narration from text content, useful for accessibility or voice assistants.

### AzureAiServicesTextAnalyticsForHealthTool
**Usage:** Extracts medical entities and relationships from healthcare text using Azure Text Analytics.

**Example:** Analyze medical records to extract diagnoses, medications, and symptoms automatically.

### AzureCogsFormRecognizerTool
**Usage:** Extracts data from forms and documents using Azure Cognitive Services Form Recognizer.

**Example:** Extract information from tax forms, applications, or receipts with structured data output.

### AzureCogsImageAnalysisTool
**Usage:** Analyzes images for content, objects, and text using Azure Cognitive Services Computer Vision.

**Example:** Detect and describe objects in images, read text, and identify landmarks or celebrities.

### AzureCogsSpeech2TextTool
**Usage:** Converts speech to text using Azure Cognitive Services Speech API with high accuracy.

**Example:** Transcribe customer service calls or meeting recordings into searchable text.

### AzureCogsText2SpeechTool
**Usage:** Synthesizes natural speech from text using Azure Cognitive Services Speech API.

**Example:** Create voiceovers for videos or generate spoken responses for voice-enabled applications.

### AzureCogsTextAnalyticsHealthTool
**Usage:** Analyzes healthcare-related text to extract medical information and relationships.

**Example:** Process clinical notes to identify medications, conditions, and treatment plans.

---

## File Management Tools

### ReadFileTool
**Usage:** Reads content from files on the local filesystem. Supports text files, code files, and more.

**Example:** Read a Python script file to analyze its contents or extract code snippets for documentation.

### WriteFileTool
**Usage:** Writes content to files on the local filesystem. Can create new files or overwrite existing ones.

**Example:** Generate a report and save it to a file, or create configuration files programmatically.

### CopyFileTool
**Usage:** Copies files from one location to another on the filesystem.

**Example:** Backup important files by copying them to a backup directory automatically.

### MoveFileTool
**Usage:** Moves files from one location to another, effectively renaming or relocating files.

**Example:** Organize downloaded files by moving them to appropriate folders based on file type.

### DeleteFileTool
**Usage:** Deletes files from the filesystem. Use with caution as this is irreversible.

**Example:** Clean up temporary files or remove outdated documents from storage.

### FileSearchTool
**Usage:** Searches for files by name or pattern on the filesystem. Supports glob patterns.

**Example:** Find all Python files in a project directory or locate configuration files by name.

### ListDirectoryTool
**Usage:** Lists files and directories in a specified path. Useful for exploring file structures.

**Example:** Browse a directory to see available files before reading or processing them.

---

## Communication Tools

### GmailSendMessage
**Usage:** Sends emails through Gmail API. Requires OAuth authentication and Gmail API setup.

**Example:** Send an automated email notification when a task is completed or an event occurs.

### GmailCreateDraft
**Usage:** Creates email drafts in Gmail without sending them. Allows review before sending.

**Example:** Generate email drafts for review, letting users edit before final sending.

### GmailGetMessage
**Usage:** Retrieves specific email messages from Gmail by message ID.

**Example:** Fetch a specific email to read its content or extract information from it.

### GmailGetThread
**Usage:** Retrieves entire email threads/conversations from Gmail.

**Example:** Get all messages in an email conversation to understand the full context.

### GmailSearch
**Usage:** Searches Gmail inbox for emails matching specific criteria like sender, subject, or date.

**Example:** Find all emails from a specific sender or containing certain keywords in the subject.

### O365SendMessage
**Usage:** Sends emails through Microsoft Office 365/Outlook. Requires Microsoft Graph API authentication.

**Example:** Send automated emails from a corporate Outlook account for notifications or reports.

### O365CreateDraftMessage
**Usage:** Creates email drafts in Office 365 without sending them immediately.

**Example:** Generate email drafts for business communications that need approval before sending.

### O365SearchEmails
**Usage:** Searches Office 365 mailbox for emails matching search criteria.

**Example:** Find all emails related to a specific project or from a particular client.

### O365SearchEvents
**Usage:** Searches calendar events in Office 365. Find meetings, appointments, and schedules.

**Example:** Check if a meeting time is available or find all events for a specific date.

### O365SendEvent
**Usage:** Creates and sends calendar events/invitations in Office 365.

**Example:** Automatically schedule meetings and send calendar invites to participants.

### SlackSendMessage
**Usage:** Sends messages to Slack channels or users. Requires Slack API token and permissions.

**Example:** Send notifications to a Slack channel when a process completes or an alert is triggered.

### SlackGetMessage
**Usage:** Retrieves messages from Slack channels or direct messages.

**Example:** Fetch recent messages from a channel to understand context or extract information.

### SlackGetChannel
**Usage:** Gets information about Slack channels including members, purpose, and settings.

**Example:** List all available channels or get details about a specific channel.

### SlackScheduleMessage
**Usage:** Schedules messages to be sent later in Slack. Useful for reminders or delayed notifications.

**Example:** Schedule a reminder message to be sent tomorrow morning or at a specific time.

---

## Database Tools

### QuerySQLDatabaseTool
**Usage:** Executes SQL queries against a SQL database. Supports PostgreSQL, MySQL, SQLite, and more.

**Example:** Query a database to find customer information or generate reports from stored data.

### InfoSQLDatabaseTool
**Usage:** Retrieves schema information about database tables, columns, and relationships.

**Example:** Get table structures to understand database schema before writing queries.

### ListSQLDatabaseTool
**Usage:** Lists all tables in a SQL database. Helps discover available data sources.

**Example:** List all tables in a database to see what data is available for querying.

### QuerySQLCheckerTool
**Usage:** Validates SQL queries for syntax errors and potential issues before execution.

**Example:** Check if a SQL query is valid and safe before running it on production data.

### QuerySQLDataBaseTool
**Usage:** Alternative SQL query tool with additional features for complex database operations.

**Example:** Execute complex queries with joins, aggregations, and subqueries across multiple tables.

### QueryCassandraDatabaseTool
**Usage:** Executes CQL (Cassandra Query Language) queries against Apache Cassandra databases.

**Example:** Query a Cassandra database to retrieve time-series data or distributed records.

### GetSchemaCassandraDatabaseTool
**Usage:** Retrieves schema information from Cassandra including keyspaces, tables, and columns.

**Example:** Understand the structure of a Cassandra database before writing queries.

### GetTableDataCassandraDatabaseTool
**Usage:** Retrieves sample data from Cassandra tables to understand data structure.

**Example:** Get a preview of data in a Cassandra table to see what information is available.

### QuerySparkSQLTool
**Usage:** Executes Spark SQL queries for big data processing. Works with Spark DataFrames and datasets.

**Example:** Process large datasets using Spark SQL for analytics and data transformations.

### InfoSparkSQLTool
**Usage:** Gets schema information from Spark SQL databases and DataFrames.

**Example:** Understand the structure of Spark DataFrames before writing complex queries.

### ListSparkSQLTool
**Usage:** Lists available tables and DataFrames in Spark SQL context.

**Example:** Discover what data sources are available in a Spark session.

### QueryCheckerTool
**Usage:** Validates Spark SQL queries for correctness and optimization opportunities.

**Example:** Check Spark SQL queries for errors and suggest optimizations before execution.

---

## Financial Tools

### PolygonAggregates
**Usage:** Retrieves aggregated stock market data (OHLCV) from Polygon.io for historical analysis.

**Example:** Get daily stock price data for AAPL over the past month to analyze trends.

### PolygonFinancials
**Usage:** Fetches financial statements and fundamental data for companies from Polygon.io.

**Example:** Retrieve income statements, balance sheets, and cash flow data for financial analysis.

### PolygonLastQuote
**Usage:** Gets the latest bid/ask quotes for stocks from Polygon.io in real-time.

**Example:** Get current market quotes to see the latest bid and ask prices for a stock.

### PolygonTickerNews
**Usage:** Retrieves news articles related to specific stock tickers from Polygon.io.

**Example:** Get recent news about Tesla (TSLA) to understand market sentiment.

### BalanceSheets
**Usage:** Accesses balance sheet data for companies from financial datasets.

**Example:** Retrieve balance sheet information to analyze a company's assets and liabilities.

### CashFlowStatements
**Usage:** Fetches cash flow statements showing company cash inflows and outflows.

**Example:** Analyze a company's cash flow to understand its financial health and liquidity.

### IncomeStatements
**Usage:** Retrieves income statements (profit & loss) for companies from financial datasets.

**Example:** Get revenue, expenses, and profit data to evaluate company performance.

### YahooFinanceNewsTool
**Usage:** Fetches financial news from Yahoo Finance related to stocks, markets, and companies.

**Example:** Get the latest financial news about Apple to stay updated on market developments.

---

## Web & Browser Tools

### NavigateTool
**Usage:** Navigates to a URL using Playwright browser automation. Opens web pages programmatically.

**Example:** Navigate to a website to scrape content or interact with web applications.

### ClickTool
**Usage:** Clicks on elements on a web page using Playwright. Interacts with buttons, links, and forms.

**Example:** Click a "Submit" button on a form or navigate by clicking links on a webpage.

### ExtractTextTool
**Usage:** Extracts all text content from a web page. Useful for content scraping and analysis.

**Example:** Extract article text from a news website to summarize or analyze the content.

### ExtractHyperlinksTool
**Usage:** Extracts all hyperlinks from a web page with their URLs and anchor text.

**Example:** Get all links on a webpage to discover related pages or resources.

### CurrentWebPageTool
**Usage:** Gets information about the currently loaded web page including URL and title.

**Example:** Check what page the browser is currently viewing before performing actions.

### NavigateBackTool
**Usage:** Navigates back to the previous page in browser history.

**Example:** Go back after viewing a page to return to the previous location.

### GetElementsTool
**Usage:** Finds and retrieves specific HTML elements from a web page using selectors.

**Example:** Find all buttons, forms, or specific elements on a page for interaction.

### RequestsGetTool
**Usage:** Performs HTTP GET requests to fetch data from APIs or web pages.

**Example:** Fetch data from a REST API endpoint to retrieve information programmatically.

### RequestsPostTool
**Usage:** Sends HTTP POST requests to submit data to APIs or web services.

**Example:** Submit form data or create resources through API endpoints.

### RequestsPutTool
**Usage:** Sends HTTP PUT requests to update resources via APIs.

**Example:** Update user information or modify existing records through API calls.

### RequestsPatchTool
**Usage:** Sends HTTP PATCH requests for partial updates to resources.

**Example:** Update specific fields of a resource without replacing the entire object.

### RequestsDeleteTool
**Usage:** Sends HTTP DELETE requests to remove resources via APIs.

**Example:** Delete records or resources through API endpoints.

---

## AI/ML Tools

### BearlyInterpreterTool
**Usage:** Executes Python code in a sandboxed environment. Great for data analysis and computations.

**Example:** Run Python code to analyze data, perform calculations, or generate visualizations.

### E2BDataAnalysisTool
**Usage:** Executes data analysis code in secure cloud sandboxes. Supports Python, R, and more.

**Example:** Analyze datasets, create charts, and perform statistical analysis in a secure environment.

### SceneXplainTool
**Usage:** Generates detailed descriptions of images using AI. Analyzes visual content comprehensively.

**Example:** Describe what's happening in a photo, identify objects, and explain the scene context.

### SteamshipImageGenerationTool
**Usage:** Generates images from text descriptions using AI image generation models.

**Example:** Create images based on prompts like "a sunset over mountains" or "a futuristic city."

### EdenAiExplicitImageTool
**Usage:** Detects explicit or inappropriate content in images using Eden AI's moderation API.

**Example:** Filter out inappropriate images from user uploads or content feeds.

### EdenAiObjectDetectionTool
**Usage:** Detects and identifies objects in images with bounding boxes and labels.

**Example:** Identify all cars, people, and objects in a street scene image.

### EdenAiParsingIDTool
**Usage:** Extracts information from ID documents like passports, driver's licenses, and IDs.

**Example:** Automatically extract name, date of birth, and ID number from a scanned ID card.

### EdenAiParsingInvoiceTool
**Usage:** Extracts structured data from invoices including amounts, dates, and line items.

**Example:** Parse invoice PDFs to extract billing information for accounting systems.

### EdenAiSpeechToTextTool
**Usage:** Converts speech audio to text using Eden AI's multi-provider speech recognition.

**Example:** Transcribe voice recordings or live audio streams into text.

### EdenAiTextToSpeechTool
**Usage:** Converts text to natural speech using Eden AI's text-to-speech services.

**Example:** Generate voice narration from text for accessibility or voice assistants.

### EdenAiTextModerationTool
**Usage:** Detects inappropriate, toxic, or harmful content in text using AI moderation.

**Example:** Filter out offensive comments or detect hate speech in user-generated content.

### ElevenLabsText2SpeechTool
**Usage:** Converts text to high-quality speech using ElevenLabs' advanced voice synthesis.

**Example:** Create natural-sounding voiceovers with various voice options and styles.

### GoogleCloudTextToSpeechTool
**Usage:** Synthesizes speech from text using Google Cloud Text-to-Speech API.

**Example:** Generate speech in multiple languages and voices for global applications.

---

## Productivity Tools

### HumanInputRun
**Usage:** Pauses agent execution to request input from a human user. Enables interactive workflows.

**Example:** Ask a user to approve an action before proceeding, or get clarification on ambiguous requests.

### StdInInquireTool
**Usage:** Reads input from standard input (stdin) for command-line interactions.

**Example:** Get user input in CLI applications or scripts that need interactive responses.

### SleepTool
**Usage:** Pauses execution for a specified duration. Useful for rate limiting or delays.

**Example:** Add delays between API calls to respect rate limits or create timed workflows.

### ShellTool
**Usage:** Executes shell commands on the system. Powerful but use with caution for security.

**Example:** Run system commands like listing files, checking system status, or executing scripts.

### JsonGetValueTool
**Usage:** Extracts specific values from JSON data using JSONPath or key navigation.

**Example:** Get the "price" field from a JSON response: `{"product": {"price": 99.99}}`.

### JsonListKeysTool
**Usage:** Lists all available keys in a JSON object to discover its structure.

**Example:** See what fields are available in a JSON response before extracting specific values.

---

## Knowledge & Research Tools

### ArxivQueryRun
**Usage:** Searches arXiv for academic papers and research articles. Great for scientific queries.

**Example:** Find recent papers on "machine learning" or "quantum computing" from arXiv.

### PubmedQueryRun
**Usage:** Searches PubMed for medical and scientific research papers and articles.

**Example:** Find research papers about "diabetes treatment" or "cancer immunotherapy."

### WikipediaQueryRun
**Usage:** Searches and retrieves information from Wikipedia articles.

**Example:** Get information about historical events, people, or concepts from Wikipedia.

### GoogleBooksQueryRun
**Usage:** Searches Google Books to find books, authors, and book information.

**Example:** Find books about a specific topic or get information about a particular author.

### MerriamWebsterQueryRun
**Usage:** Looks up word definitions, synonyms, and usage examples from Merriam-Webster dictionary.

**Example:** Get definitions and examples for words to help with writing or understanding.

### StackExchangeTool
**Usage:** Searches Stack Overflow and other Stack Exchange sites for programming questions and answers.

**Example:** Find solutions to coding problems or technical questions from Stack Overflow.

### RedditSearchRun
**Usage:** Searches Reddit for posts, comments, and discussions on various topics.

**Example:** Find discussions about "Python programming" or "productivity tips" on Reddit.

### NasaAction
**Usage:** Accesses NASA APIs to get space data, images, and information about space missions.

**Example:** Get images from Mars rovers, information about asteroids, or space mission data.

### OpenWeatherMapQueryRun
**Usage:** Retrieves weather information for locations worldwide using OpenWeatherMap API.

**Example:** Get current weather, forecasts, or historical weather data for any city.

### GooglePlacesTool
**Usage:** Searches for places, businesses, and locations using Google Places API.

**Example:** Find restaurants near a location, get business hours, or find points of interest.

### WolframAlphaQueryRun
**Usage:** Queries Wolfram Alpha for computational answers, math solutions, and factual data.

**Example:** Solve math problems, get unit conversions, or answer factual questions using Wolfram Alpha.

### YouTubeSearchTool
**Usage:** Searches YouTube for videos matching search queries. Returns video information and links.

**Example:** Find tutorial videos about "Python programming" or "cooking recipes" on YouTube.

---

## Integration Tools

### ZapierNLAListActions
**Usage:** Lists available Zapier actions that can be triggered. Discovers automation possibilities.

**Example:** See what actions are available in Zapier like "Send email" or "Create calendar event."

### ZapierNLARunAction
**Usage:** Executes Zapier actions to trigger automations and integrations with other services.

**Example:** Trigger a Zapier workflow to send a Slack message when an event occurs.

### IFTTTWebhook
**Usage:** Triggers IFTTT (If This Then That) webhooks to activate automations and applets.

**Example:** Trigger an IFTTT automation to turn on smart lights or send notifications.

### ConneryAction
**Usage:** Executes actions through Connery platform for workflow automation and integrations.

**Example:** Run automated workflows that connect multiple services and applications.

### AIPluginTool
**Usage:** Integrates with AI plugins and extensions to extend functionality with third-party tools.

**Example:** Use plugins to add capabilities like translation, summarization, or specialized functions.

### BaseGraphQLTool
**Usage:** Base tool for executing GraphQL queries against GraphQL APIs.

**Example:** Query a GraphQL API to fetch data from services like GitHub, Shopify, or custom APIs.

### DataheraldTextToSQL
**Usage:** Converts natural language questions into SQL queries automatically using AI.

**Example:** Ask "What are the top 10 customers by revenue?" and it generates the SQL query.

### CogniswitchKnowledgeRequest
**Usage:** Queries Cogniswitch knowledge base to retrieve information from connected data sources.

**Example:** Ask questions and get answers from your organization's knowledge base.

### CogniswitchKnowledgeSourceFile
**Usage:** Adds files as knowledge sources to Cogniswitch knowledge base.

**Example:** Upload documents to make them searchable through the knowledge base.

### CogniswitchKnowledgeSourceURL
**Usage:** Adds web URLs as knowledge sources to Cogniswitch knowledge base.

**Example:** Add website content to the knowledge base for retrieval and answering.

### CogniswitchKnowledgeStatus
**Usage:** Checks the status of knowledge sources and indexing in Cogniswitch.

**Example:** Verify if documents have been successfully indexed and are available for queries.

### PowerBITool (InfoPowerBITool, ListPowerBITool, QueryPowerBITool)
**Usage:** Interacts with Microsoft Power BI to query datasets, list reports, and get information.

**Example:** Query Power BI datasets to get business intelligence insights and analytics.

### SteamWebAPIQueryRun
**Usage:** Queries Steam Web API to get game information, player data, and Steam store information.

**Example:** Get information about games, check player achievements, or search the Steam store.

### ZenGuardTool
**Usage:** Security tool that detects and prevents prompt injection attacks and malicious inputs.

**Example:** Protect your chatbot from users trying to inject malicious prompts or bypass safety measures.

---

## Recommended Tools for Your Chatbot

Based on your current chatbot implementation (which includes DuckDuckGo search, calculator, and stock price tools), here are some highly recommended tools to enhance functionality:

### 1. **TavilySearchResults** or **TavilyAnswer**
   - **Why:** Better than basic DuckDuckGo for AI applications. Returns results optimized for LLM understanding.
   - **Use Case:** Replace or complement DuckDuckGoSearchRun for more intelligent search results.
   - **Example:** User asks complex questions and gets AI-optimized answers instead of raw search results.

### 2. **OpenWeatherMapQueryRun**
   - **Why:** Adds weather functionality that users frequently request.
   - **Use Case:** Answer questions like "What's the weather in New York?" or "Will it rain tomorrow?"
   - **Example:** Provides current weather, forecasts, and historical weather data.

### 3. **WikipediaQueryRun**
   - **Why:** Quick access to factual information and general knowledge.
   - **Use Case:** Answer questions about history, science, people, places, and concepts.
   - **Example:** User asks "Tell me about the Eiffel Tower" and gets Wikipedia information.

### 4. **WolframAlphaQueryRun**
   - **Why:** Excellent for math, calculations, unit conversions, and factual queries.
   - **Use Case:** Complements your calculator tool with advanced math, conversions, and computational answers.
   - **Example:** Solve complex equations, convert units, or answer factual questions with precision.

### 5. **ArxivQueryRun**
   - **Why:** Access to cutting-edge research papers for technical and scientific queries.
   - **Use Case:** When users ask about recent research, scientific topics, or academic information.
   - **Example:** Find and summarize recent papers on "large language models" or "quantum computing."

### 6. **ReadFileTool** and **WriteFileTool**
   - **Why:** Enable file operations for users who want to work with files.
   - **Use Case:** Read code files, write reports, or manage documents through the chatbot.
   - **Example:** User asks "Read my config file" or "Save this conversation to a file."

### 7. **JsonGetValueTool** and **JsonListKeysTool**
   - **Why:** Help parse and work with JSON data from APIs or user inputs.
   - **Use Case:** Extract specific data from API responses or JSON structures.
   - **Example:** Parse stock API responses or extract information from JSON data.

### 8. **YahooFinanceNewsTool**
   - **Why:** Complements your stock price tool with financial news.
   - **Use Case:** When users ask about stock market news or want context about stock movements.
   - **Example:** Get news about why a stock price changed or market trends.

### 9. **StackExchangeTool**
   - **Why:** Access to programming Q&A for technical support.
   - **Use Case:** Find solutions to coding problems or technical questions.
   - **Example:** User asks "How do I fix this Python error?" and gets Stack Overflow solutions.

### 10. **YouTubeSearchTool**
   - **Why:** Find tutorial videos and educational content.
   - **Use Case:** When users want video tutorials or visual explanations.
   - **Example:** Find tutorial videos about a programming topic or how-to guides.

### 11. **E2BDataAnalysisTool** or **BearlyInterpreterTool**
   - **Why:** Execute Python code for data analysis and computations beyond basic calculator.
   - **Use Case:** Perform complex calculations, data analysis, or generate visualizations.
   - **Example:** User asks "Analyze this dataset" or "Create a chart of sales data."

### 12. **GoogleBooksQueryRun**
   - **Why:** Find books and reading recommendations.
   - **Use Case:** When users ask for book recommendations or information about books.
   - **Example:** Find books about "machine learning" or get information about a specific book.

### Priority Implementation Order:
1. **TavilySearchResults** - Immediate upgrade to search functionality
2. **OpenWeatherMapQueryRun** - High user demand, easy integration
3. **WikipediaQueryRun** - Quick factual answers, no API key needed (usually)
4. **WolframAlphaQueryRun** - Advanced math and conversions
5. **ReadFileTool/WriteFileTool** - File operations for power users
6. **YahooFinanceNewsTool** - Complements existing stock tool

These tools will significantly enhance your chatbot's capabilities while maintaining the simplicity of your current architecture.

---

## Notes

- Most tools require API keys or authentication. Check each tool's documentation for setup requirements.
- Some tools may have usage limits or costs associated with them.
- Always implement proper error handling when adding new tools.
- Consider rate limiting for tools that make external API calls.
- Test tools thoroughly before deploying to production.

---

*Generated for LangGraph Chatbot Project - December 2025*

