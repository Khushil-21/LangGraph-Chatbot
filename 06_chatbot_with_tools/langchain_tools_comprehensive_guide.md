# LangChain Community Tools - Comprehensive Guide

This document provides a detailed overview of all available tools in the LangChain Community package, including usage explanations, examples, cost information, and implementation effort.

---

## Understanding Tags

### Cost Tags
- **🆓 Free/Open Source:** No API key required or completely free to use
- **🎁 Free Tier:** Has a free tier but may require API key/signup
- **💰 Paid:** Requires paid subscription or credits

### Effort Tags
- **🟢 Low Effort:** 15-20 minutes implementation time
- **🟡 Medium Effort:** 25-40 minutes implementation time
- **🔴 High Effort:** 40+ minutes implementation time

---

## Table of Contents

1. [Core Tools](#core-tools)
2. [Search Tools](#search-tools)
3. [AI Network Tools](#ai-network-tools)
4. [Azure Services](#azure-services)
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
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Base class for creating custom tools in LangChain. Inherit from this to build your own tool implementations.

**Example:** Create a custom tool that extends BaseTool to add domain-specific functionality like weather queries or API integrations.

### Tool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Simple tool wrapper for functions that don't require structured input/output. Use this for basic function-to-tool conversions.

**Example:** Convert a Python function like `def greet(name): return f"Hello {name}"` into a LangChain tool that can be used by agents.

### StructuredTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Tool wrapper that enforces structured input/output using Pydantic models. Perfect for tools requiring validated parameters.

**Example:** Create a tool with strict typing like a calculator that requires two floats and an operation string, ensuring type safety.

### tool (decorator)
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Decorator to convert Python functions into LangChain tools automatically. Simplifies tool creation with minimal code.

**Example:** Add `@tool` decorator above a function to make it instantly available to LangChain agents without manual configuration.

---

## Search Tools

### DuckDuckGoSearchRun
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Performs web searches using DuckDuckGo search engine. Returns search results as text. No API key required.

**Example:** User asks "What is the weather in New York?" and the tool searches DuckDuckGo to find current weather information.

**Note:** Already integrated in your chatbot.

### DuckDuckGoSearchResults
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Similar to DuckDuckGoSearchRun but returns structured search results with titles, snippets, and URLs.

**Example:** Returns formatted results like `[{"title": "...", "snippet": "...", "url": "..."}]` for better result parsing.

### BingSearchRun
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Performs web searches using Microsoft Bing search API. Requires Bing API key for authentication.

**Example:** Search for "latest AI developments" and get comprehensive results from Bing's search index.

### BingSearchResults
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Returns structured Bing search results with metadata including relevance scores and publication dates.

**Example:** Get ranked search results with additional context like date published and domain information.

### GoogleSearchRun
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Executes searches using Google Custom Search API. Requires Google API key and search engine ID.

**Example:** Search for "Python tutorials" and retrieve results from Google's vast search index.

### GoogleSearchResults
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Returns structured Google search results with rich metadata including images, videos, and knowledge graph data.

**Example:** Get comprehensive search results including featured snippets, related questions, and multimedia content.

### GoogleSerperRun
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Uses Serper.dev API for Google search results. Faster and more cost-effective than direct Google API.

**Example:** Search for "best restaurants near me" and get instant results with location-based information.

### GoogleSerperResults
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Returns structured results from Serper.dev with enhanced metadata and faster response times.

**Example:** Get search results with additional context like ratings, prices, and business hours for local searches.

### BraveSearch
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Performs searches using Brave Search API. Privacy-focused search engine alternative.

**Example:** Search for "cryptocurrency news" and get results from Brave's independent search index.

### TavilySearchResults
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** AI-powered search tool that returns relevant results optimized for LLM consumption. Great for RAG applications.

**Example:** Search for "quantum computing breakthroughs" and get results specifically formatted for AI understanding.

**Note:** Has a free tier with limited queries, then paid.

### TavilyAnswer
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** Returns direct answers to queries using Tavily's AI search, perfect for factual questions.

**Example:** Ask "What is the capital of France?" and get a direct answer instead of search result links.

### JinaSearch
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Neural search tool that understands semantic meaning of queries, not just keywords.

**Example:** Search for "ways to save money" and get results about budgeting, investing, and financial planning even if those exact words aren't in the results.

### SearxSearchResults
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Meta-search engine that aggregates results from multiple search engines. Privacy-focused and customizable.

**Example:** Search across Google, Bing, and DuckDuckGo simultaneously to get comprehensive results.

**Note:** Requires setting up a Searx instance or using a public one.

### SearxSearchRun
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Executes searches using self-hosted or public Searx instances for aggregated search results.

**Example:** Get combined results from multiple search engines in a single query for better coverage.

### MojeekSearch
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Alternative search engine that provides independent search results without tracking.

**Example:** Search for information while maintaining privacy, as Mojeek doesn't track user behavior.

### SearchAPIRun
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Unified search API that aggregates results from multiple search engines and sources.

**Example:** Get comprehensive search results from various sources in a single API call.

### SearchAPIResults
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Returns structured results from SearchAPI with metadata from multiple search engines.

**Example:** Receive formatted results with source attribution and relevance scores from various search providers.

### MetaphorSearchResults
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** AI-powered search that finds content based on meaning and context, not just keywords.

**Example:** Search for "articles about sustainable energy" and get semantically related content even if those exact words aren't used.

### YouSearchTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Search tool using You.com's AI-powered search engine with conversational results.

**Example:** Get natural language search results that read like answers rather than just links.

---

## AI Network Tools

### AINAppOps
**Tags:** 💰 Paid | 🔴 High Effort

**Usage:** Manages applications on the AI Network blockchain. Create, update, and manage AI applications.

**Example:** Deploy a new AI model or service on the AI Network blockchain platform.

### AINOwnerOps
**Tags:** 💰 Paid | 🔴 High Effort

**Usage:** Handles ownership operations for AI Network resources. Transfer ownership, manage permissions.

**Example:** Transfer ownership of an AI Network application to another user or organization.

### AINRuleOps
**Tags:** 💰 Paid | 🔴 High Effort

**Usage:** Manages rules and policies for AI Network applications. Set up governance and access controls.

**Example:** Configure rules that determine who can access or modify an AI Network application.

### AINTransfer
**Tags:** 💰 Paid | 🔴 High Effort

**Usage:** Transfers tokens or resources within the AI Network ecosystem.

**Example:** Transfer AI Network tokens between accounts or applications.

### AINValueOps
**Tags:** 💰 Paid | 🔴 High Effort

**Usage:** Manages value operations like deposits, withdrawals, and balance queries on AI Network.

**Example:** Check balance or transfer value between AI Network accounts.

---

## Azure Services

### AzureAiServicesDocumentIntelligenceTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Extracts text, tables, and structure from documents using Azure Document Intelligence. Perfect for PDF processing.

**Example:** Extract all text and tables from a PDF invoice to analyze billing information automatically.

### AzureAiServicesImageAnalysisTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Analyzes images to detect objects, faces, text, and generate descriptions using Azure Computer Vision.

**Example:** Analyze a photo to identify objects, read text in images, and generate captions automatically.

### AzureAiServicesSpeechToTextTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Converts spoken audio to text using Azure Speech Services. Supports multiple languages.

**Example:** Transcribe a voice recording or live audio stream into written text for processing.

### AzureAiServicesTextToSpeechTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Converts text to natural-sounding speech using Azure Neural Voices. Multiple voice options available.

**Example:** Generate audio narration from text content, useful for accessibility or voice assistants.

### AzureAiServicesTextAnalyticsForHealthTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Extracts medical entities and relationships from healthcare text using Azure Text Analytics.

**Example:** Analyze medical records to extract diagnoses, medications, and symptoms automatically.

### AzureCogsFormRecognizerTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Extracts data from forms and documents using Azure Cognitive Services Form Recognizer.

**Example:** Extract information from tax forms, applications, or receipts with structured data output.

### AzureCogsImageAnalysisTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Analyzes images for content, objects, and text using Azure Cognitive Services Computer Vision.

**Example:** Detect and describe objects in images, read text, and identify landmarks or celebrities.

### AzureCogsSpeech2TextTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Converts speech to text using Azure Cognitive Services Speech API with high accuracy.

**Example:** Transcribe customer service calls or meeting recordings into searchable text.

### AzureCogsText2SpeechTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Synthesizes natural speech from text using Azure Cognitive Services Speech API.

**Example:** Create voiceovers for videos or generate spoken responses for voice-enabled applications.

### AzureCogsTextAnalyticsHealthTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Analyzes healthcare-related text to extract medical information and relationships.

**Example:** Process clinical notes to identify medications, conditions, and treatment plans.

---

## File Management Tools

### ReadFileTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Reads content from files on the local filesystem. Supports text files, code files, and more.

**Example:** Read a Python script file to analyze its contents or extract code snippets for documentation.

### WriteFileTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Writes content to files on the local filesystem. Can create new files or overwrite existing ones.

**Example:** Generate a report and save it to a file, or create configuration files programmatically.

### CopyFileTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Copies files from one location to another on the filesystem.

**Example:** Backup important files by copying them to a backup directory automatically.

### MoveFileTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Moves files from one location to another, effectively renaming or relocating files.

**Example:** Organize downloaded files by moving them to appropriate folders based on file type.

### DeleteFileTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Deletes files from the filesystem. Use with caution as this is irreversible.

**Example:** Clean up temporary files or remove outdated documents from storage.

### FileSearchTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Searches for files by name or pattern on the filesystem. Supports glob patterns.

**Example:** Find all Python files in a project directory or locate configuration files by name.

### ListDirectoryTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Lists files and directories in a specified path. Useful for exploring file structures.

**Example:** Browse a directory to see available files before reading or processing them.

---

## Communication Tools

### GmailSendMessage
**Tags:** 🆓 Free/Open Source | 🔴 High Effort

**Usage:** Sends emails through Gmail API. Requires OAuth authentication and Gmail API setup.

**Example:** Send an automated email notification when a task is completed or an event occurs.

**Note:** Free but requires Google Cloud project setup and OAuth flow.

### GmailCreateDraft
**Tags:** 🆓 Free/Open Source | 🔴 High Effort

**Usage:** Creates email drafts in Gmail without sending them. Allows review before sending.

**Example:** Generate email drafts for review, letting users edit before final sending.

### GmailGetMessage
**Tags:** 🆓 Free/Open Source | 🔴 High Effort

**Usage:** Retrieves specific email messages from Gmail by message ID.

**Example:** Fetch a specific email to read its content or extract information from it.

### GmailGetThread
**Tags:** 🆓 Free/Open Source | 🔴 High Effort

**Usage:** Retrieves entire email threads/conversations from Gmail.

**Example:** Get all messages in an email conversation to understand the full context.

### GmailSearch
**Tags:** 🆓 Free/Open Source | 🔴 High Effort

**Usage:** Searches Gmail inbox for emails matching specific criteria like sender, subject, or date.

**Example:** Find all emails from a specific sender or containing certain keywords in the subject.

### O365SendMessage
**Tags:** 🎁 Free Tier | 🔴 High Effort

**Usage:** Sends emails through Microsoft Office 365/Outlook. Requires Microsoft Graph API authentication.

**Example:** Send automated emails from a corporate Outlook account for notifications or reports.

### O365CreateDraftMessage
**Tags:** 🎁 Free Tier | 🔴 High Effort

**Usage:** Creates email drafts in Office 365 without sending them immediately.

**Example:** Generate email drafts for business communications that need approval before sending.

### O365SearchEmails
**Tags:** 🎁 Free Tier | 🔴 High Effort

**Usage:** Searches Office 365 mailbox for emails matching search criteria.

**Example:** Find all emails related to a specific project or from a particular client.

### O365SearchEvents
**Tags:** 🎁 Free Tier | 🔴 High Effort

**Usage:** Searches calendar events in Office 365. Find meetings, appointments, and schedules.

**Example:** Check if a meeting time is available or find all events for a specific date.

### O365SendEvent
**Tags:** 🎁 Free Tier | 🔴 High Effort

**Usage:** Creates and sends calendar events/invitations in Office 365.

**Example:** Automatically schedule meetings and send calendar invites to participants.

### SlackSendMessage
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Sends messages to Slack channels or users. Requires Slack API token and permissions.

**Example:** Send notifications to a Slack channel when a process completes or an alert is triggered.

### SlackGetMessage
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Retrieves messages from Slack channels or direct messages.

**Example:** Fetch recent messages from a channel to understand context or extract information.

### SlackGetChannel
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Gets information about Slack channels including members, purpose, and settings.

**Example:** List all available channels or get details about a specific channel.

### SlackScheduleMessage
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Schedules messages to be sent later in Slack. Useful for reminders or delayed notifications.

**Example:** Schedule a reminder message to be sent tomorrow morning or at a specific time.

---

## Database Tools

### QuerySQLDatabaseTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Executes SQL queries against a SQL database. Supports PostgreSQL, MySQL, SQLite, and more.

**Example:** Query a database to find customer information or generate reports from stored data.

### InfoSQLDatabaseTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Retrieves schema information about database tables, columns, and relationships.

**Example:** Get table structures to understand database schema before writing queries.

### ListSQLDatabaseTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Lists all tables in a SQL database. Helps discover available data sources.

**Example:** List all tables in a database to see what data is available for querying.

### QuerySQLCheckerTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Validates SQL queries for syntax errors and potential issues before execution.

**Example:** Check if a SQL query is valid and safe before running it on production data.

### QuerySQLDataBaseTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Alternative SQL query tool with additional features for complex database operations.

**Example:** Execute complex queries with joins, aggregations, and subqueries across multiple tables.

### QueryCassandraDatabaseTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Executes CQL (Cassandra Query Language) queries against Apache Cassandra databases.

**Example:** Query a Cassandra database to retrieve time-series data or distributed records.

### GetSchemaCassandraDatabaseTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Retrieves schema information from Cassandra including keyspaces, tables, and columns.

**Example:** Understand the structure of a Cassandra database before writing queries.

### GetTableDataCassandraDatabaseTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Retrieves sample data from Cassandra tables to understand data structure.

**Example:** Get a preview of data in a Cassandra table to see what information is available.

### QuerySparkSQLTool
**Tags:** 🆓 Free/Open Source | 🔴 High Effort

**Usage:** Executes Spark SQL queries for big data processing. Works with Spark DataFrames and datasets.

**Example:** Process large datasets using Spark SQL for analytics and data transformations.

### InfoSparkSQLTool
**Tags:** 🆓 Free/Open Source | 🔴 High Effort

**Usage:** Gets schema information from Spark SQL databases and DataFrames.

**Example:** Understand the structure of Spark DataFrames before writing complex queries.

### ListSparkSQLTool
**Tags:** 🆓 Free/Open Source | 🔴 High Effort

**Usage:** Lists available tables and DataFrames in Spark SQL context.

**Example:** Discover what data sources are available in a Spark session.

### QueryCheckerTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Validates Spark SQL queries for correctness and optimization opportunities.

**Example:** Check Spark SQL queries for errors and suggest optimizations before execution.

---

## Financial Tools

### PolygonAggregates
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Retrieves aggregated stock market data (OHLCV) from Polygon.io for historical analysis.

**Example:** Get daily stock price data for AAPL over the past month to analyze trends.

### PolygonFinancials
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Fetches financial statements and fundamental data for companies from Polygon.io.

**Example:** Retrieve income statements, balance sheets, and cash flow data for financial analysis.

### PolygonLastQuote
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Gets the latest bid/ask quotes for stocks from Polygon.io in real-time.

**Example:** Get current market quotes to see the latest bid and ask prices for a stock.

### PolygonTickerNews
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Retrieves news articles related to specific stock tickers from Polygon.io.

**Example:** Get recent news about Tesla (TSLA) to understand market sentiment.

### BalanceSheets
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Accesses balance sheet data for companies from financial datasets.

**Example:** Retrieve balance sheet information to analyze a company's assets and liabilities.

### CashFlowStatements
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Fetches cash flow statements showing company cash inflows and outflows.

**Example:** Analyze a company's cash flow to understand its financial health and liquidity.

### IncomeStatements
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Retrieves income statements (profit & loss) for companies from financial datasets.

**Example:** Get revenue, expenses, and profit data to evaluate company performance.

### YahooFinanceNewsTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Fetches financial news from Yahoo Finance related to stocks, markets, and companies.

**Example:** Get the latest financial news about Apple to stay updated on market developments.

---

## Web & Browser Tools

### NavigateTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Navigates to a URL using Playwright browser automation. Opens web pages programmatically.

**Example:** Navigate to a website to scrape content or interact with web applications.

**Note:** Requires Playwright installation.

### ClickTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Clicks on elements on a web page using Playwright. Interacts with buttons, links, and forms.

**Example:** Click a "Submit" button on a form or navigate by clicking links on a webpage.

### ExtractTextTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Extracts all text content from a web page. Useful for content scraping and analysis.

**Example:** Extract article text from a news website to summarize or analyze the content.

### ExtractHyperlinksTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Extracts all hyperlinks from a web page with their URLs and anchor text.

**Example:** Get all links on a webpage to discover related pages or resources.

### CurrentWebPageTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Gets information about the currently loaded web page including URL and title.

**Example:** Check what page the browser is currently viewing before performing actions.

### NavigateBackTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Navigates back to the previous page in browser history.

**Example:** Go back after viewing a page to return to the previous location.

### GetElementsTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Finds and retrieves specific HTML elements from a web page using selectors.

**Example:** Find all buttons, forms, or specific elements on a page for interaction.

### RequestsGetTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Performs HTTP GET requests to fetch data from APIs or web pages.

**Example:** Fetch data from a REST API endpoint to retrieve information programmatically.

### RequestsPostTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Sends HTTP POST requests to submit data to APIs or web services.

**Example:** Submit form data or create resources through API endpoints.

### RequestsPutTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Sends HTTP PUT requests to update resources via APIs.

**Example:** Update user information or modify existing records through API calls.

### RequestsPatchTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Sends HTTP PATCH requests for partial updates to resources.

**Example:** Update specific fields of a resource without replacing the entire object.

### RequestsDeleteTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Sends HTTP DELETE requests to remove resources via APIs.

**Example:** Delete records or resources through API endpoints.

---

## AI/ML Tools

### BearlyInterpreterTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Executes Python code in a sandboxed environment. Great for data analysis and computations.

**Example:** Run Python code to analyze data, perform calculations, or generate visualizations.

### E2BDataAnalysisTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Executes data analysis code in secure cloud sandboxes. Supports Python, R, and more.

**Example:** Analyze datasets, create charts, and perform statistical analysis in a secure environment.

### SceneXplainTool
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** Generates detailed descriptions of images using AI. Analyzes visual content comprehensively.

**Example:** Describe what's happening in a photo, identify objects, and explain the scene context.

### SteamshipImageGenerationTool
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** Generates images from text descriptions using AI image generation models.

**Example:** Create images based on prompts like "a sunset over mountains" or "a futuristic city."

### EdenAiExplicitImageTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Detects explicit or inappropriate content in images using Eden AI's moderation API.

**Example:** Filter out inappropriate images from user uploads or content feeds.

### EdenAiObjectDetectionTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Detects and identifies objects in images with bounding boxes and labels.

**Example:** Identify all cars, people, and objects in a street scene image.

### EdenAiParsingIDTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Extracts information from ID documents like passports, driver's licenses, and IDs.

**Example:** Automatically extract name, date of birth, and ID number from a scanned ID card.

### EdenAiParsingInvoiceTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Extracts structured data from invoices including amounts, dates, and line items.

**Example:** Parse invoice PDFs to extract billing information for accounting systems.

### EdenAiSpeechToTextTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Converts speech audio to text using Eden AI's multi-provider speech recognition.

**Example:** Transcribe voice recordings or live audio streams into text.

### EdenAiTextToSpeechTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Converts text to natural speech using Eden AI's text-to-speech services.

**Example:** Generate voice narration from text for accessibility or voice assistants.

### EdenAiTextModerationTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Detects inappropriate, toxic, or harmful content in text using AI moderation.

**Example:** Filter out offensive comments or detect hate speech in user-generated content.

### ElevenLabsText2SpeechTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Converts text to high-quality speech using ElevenLabs' advanced voice synthesis.

**Example:** Create natural-sounding voiceovers with various voice options and styles.

### GoogleCloudTextToSpeechTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Synthesizes speech from text using Google Cloud Text-to-Speech API.

**Example:** Generate speech in multiple languages and voices for global applications.

---

## Productivity Tools

### HumanInputRun
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Pauses agent execution to request input from a human user. Enables interactive workflows.

**Example:** Ask a user to approve an action before proceeding, or get clarification on ambiguous requests.

### StdInInquireTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Reads input from standard input (stdin) for command-line interactions.

**Example:** Get user input in CLI applications or scripts that need interactive responses.

### SleepTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Pauses execution for a specified duration. Useful for rate limiting or delays.

**Example:** Add delays between API calls to respect rate limits or create timed workflows.

### ShellTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Executes shell commands on the system. Powerful but use with caution for security.

**Example:** Run system commands like listing files, checking system status, or executing scripts.

**Note:** Security risk - should be used carefully with proper sandboxing.

### JsonGetValueTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Extracts specific values from JSON data using JSONPath or key navigation.

**Example:** Get the "price" field from a JSON response: `{"product": {"price": 99.99}}`.

### JsonListKeysTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Lists all available keys in a JSON object to discover its structure.

**Example:** See what fields are available in a JSON response before extracting specific values.

---

## Knowledge & Research Tools

### ArxivQueryRun
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Searches arXiv for academic papers and research articles. Great for scientific queries.

**Example:** Find recent papers on "machine learning" or "quantum computing" from arXiv.

### PubmedQueryRun
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Searches PubMed for medical and scientific research papers and articles.

**Example:** Find research papers about "diabetes treatment" or "cancer immunotherapy."

### WikipediaQueryRun
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Searches and retrieves information from Wikipedia articles. No API key required.

**Example:** Get information about historical events, people, or concepts from Wikipedia.

### GoogleBooksQueryRun
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Searches Google Books to find books, authors, and book information.

**Example:** Find books about a specific topic or get information about a particular author.

### MerriamWebsterQueryRun
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Looks up word definitions, synonyms, and usage examples from Merriam-Webster dictionary.

**Example:** Get definitions and examples for words to help with writing or understanding.

### StackExchangeTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Searches Stack Overflow and other Stack Exchange sites for programming questions and answers.

**Example:** Find solutions to coding problems or technical questions from Stack Overflow.

### RedditSearchRun
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Searches Reddit for posts, comments, and discussions on various topics.

**Example:** Find discussions about "Python programming" or "productivity tips" on Reddit.

### NasaAction
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Accesses NASA APIs to get space data, images, and information about space missions.

**Example:** Get images from Mars rovers, information about asteroids, or space mission data.

### OpenWeatherMapQueryRun
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Retrieves weather information for locations worldwide using OpenWeatherMap API. Has generous free tier.

**Example:** Get current weather, forecasts, or historical weather data for any city.

### GooglePlacesTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Searches for places, businesses, and locations using Google Places API.

**Example:** Find restaurants near a location, get business hours, or find points of interest.

### WolframAlphaQueryRun
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Queries Wolfram Alpha for computational answers, math solutions, and factual data.

**Example:** Solve math problems, get unit conversions, or answer factual questions using Wolfram Alpha.

### YouTubeSearchTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Searches YouTube for videos matching search queries. Returns video information and links.

**Example:** Find tutorial videos about "Python programming" or "cooking recipes" on YouTube.

---

## Integration Tools

### ZapierNLAListActions
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Lists available Zapier actions that can be triggered. Discovers automation possibilities.

**Example:** See what actions are available in Zapier like "Send email" or "Create calendar event."

### ZapierNLARunAction
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Executes Zapier actions to trigger automations and integrations with other services.

**Example:** Trigger a Zapier workflow to send a Slack message when an event occurs.

### IFTTTWebhook
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Triggers IFTTT (If This Then That) webhooks to activate automations and applets.

**Example:** Trigger an IFTTT automation to turn on smart lights or send notifications.

### ConneryAction
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Executes actions through Connery platform for workflow automation and integrations.

**Example:** Run automated workflows that connect multiple services and applications.

### AIPluginTool
**Tags:** 🆓 Free/Open Source | 🟡 Medium Effort

**Usage:** Integrates with AI plugins and extensions to extend functionality with third-party tools.

**Example:** Use plugins to add capabilities like translation, summarization, or specialized functions.

### BaseGraphQLTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Usage:** Base tool for executing GraphQL queries against GraphQL APIs.

**Example:** Query a GraphQL API to fetch data from services like GitHub, Shopify, or custom APIs.

### DataheraldTextToSQL
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** Converts natural language questions into SQL queries automatically using AI.

**Example:** Ask "What are the top 10 customers by revenue?" and it generates the SQL query.

### CogniswitchKnowledgeRequest
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** Queries Cogniswitch knowledge base to retrieve information from connected data sources.

**Example:** Ask questions and get answers from your organization's knowledge base.

### CogniswitchKnowledgeSourceFile
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** Adds files as knowledge sources to Cogniswitch knowledge base.

**Example:** Upload documents to make them searchable through the knowledge base.

### CogniswitchKnowledgeSourceURL
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** Adds web URLs as knowledge sources to Cogniswitch knowledge base.

**Example:** Add website content to the knowledge base for retrieval and answering.

### CogniswitchKnowledgeStatus
**Tags:** 💰 Paid | 🟢 Low Effort

**Usage:** Checks the status of knowledge sources and indexing in Cogniswitch.

**Example:** Verify if documents have been successfully indexed and are available for queries.

### InfoPowerBITool
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** Gets information about Power BI datasets and reports.

**Example:** List available Power BI reports and datasets for analysis.

### ListPowerBITool
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** Lists available Power BI reports and datasets in your workspace.

**Example:** Discover what Power BI resources are available for querying.

### QueryPowerBITool
**Tags:** 💰 Paid | 🟡 Medium Effort

**Usage:** Queries Power BI datasets to get business intelligence insights.

**Example:** Get sales data, KPIs, or other business metrics from Power BI.

### SteamWebAPIQueryRun
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Usage:** Queries Steam Web API to get game information, player data, and Steam store information.

**Example:** Get information about games, check player achievements, or search the Steam store.

### ZenGuardTool
**Tags:** 🎁 Free Tier | 🟡 Medium Effort

**Usage:** Security tool that detects and prevents prompt injection attacks and malicious inputs.

**Example:** Protect your chatbot from users trying to inject malicious prompts or bypass safety measures.

---

## Recommended Tools for Your Chatbot

Based on your current chatbot implementation and the criteria of **Low/Medium effort** and **Free/Free Tier**, here are the top recommendations:

### Tier 1: Must-Have Tools (High Value, Easy Integration)

#### 1. WikipediaQueryRun
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Why:** Provides instant access to comprehensive general knowledge without API keys.

**Integration Time:** 15 minutes

**Use Case:** Answer questions about history, science, geography, people, and general knowledge.

**Example:** User asks "Tell me about the Eiffel Tower" → Get Wikipedia summary instantly.

**Code Snippet:**
```python
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
```

---

#### 2. OpenWeatherMapQueryRun
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Why:** Weather queries are extremely common. Free tier includes 1000 calls/day which is generous.

**Integration Time:** 20 minutes (including API key signup)

**Use Case:** Get current weather, forecasts, and weather conditions for any location.

**Example:** "What's the weather in Tokyo?" → Current temperature, conditions, forecast.

**Code Snippet:**
```python
from langchain_community.tools import OpenWeatherMapQueryRun
from langchain_community.utilities import OpenWeatherMapAPIWrapper

weather_tool = OpenWeatherMapQueryRun(api_wrapper=OpenWeatherMapAPIWrapper())
```

---

#### 3. YahooFinanceNewsTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Why:** Complements your existing stock price tool perfectly. No API key required.

**Integration Time:** 10 minutes

**Use Case:** Get financial news about stocks, markets, and companies.

**Example:** "What's the news about AAPL?" → Recent news articles about Apple stock.

**Code Snippet:**
```python
from langchain_community.tools import YahooFinanceNewsTool

finance_news_tool = YahooFinanceNewsTool()
```

---

#### 4. ArxivQueryRun
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Why:** Access to academic research and papers. Great for technical/scientific questions.

**Integration Time:** 15 minutes

**Use Case:** Find and summarize academic papers on various topics.

**Example:** "Find papers about transformer models" → Recent arXiv papers with abstracts.

**Code Snippet:**
```python
from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper

arxiv_tool = ArxivQueryRun(api_wrapper=ArxivAPIWrapper())
```

---

#### 5. YouTubeSearchTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Why:** Find educational videos and tutorials. Very useful for learning resources.

**Integration Time:** 15 minutes

**Use Case:** Search for tutorial videos and educational content.

**Example:** "Find Python tutorial videos" → Links to relevant YouTube videos.

**Code Snippet:**
```python
from langchain_community.tools import YouTubeSearchTool

youtube_tool = YouTubeSearchTool()
```

---

### Tier 2: High Value Tools (Medium Effort, Worth It)

#### 6. WolframAlphaQueryRun
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Why:** Advanced calculations, unit conversions, and factual queries. Complements your calculator.

**Integration Time:** 20 minutes (including API signup)

**Use Case:** Solve complex math, conversions, and computational questions.

**Example:** "Convert 100 USD to EUR" or "Solve x^2 + 5x + 6 = 0"

**Code Snippet:**
```python
from langchain_community.tools import WolframAlphaQueryRun
from langchain_community.utilities import WolframAlphaAPIWrapper

wolfram_tool = WolframAlphaQueryRun(api_wrapper=WolframAlphaAPIWrapper())
```

---

#### 7. ReadFileTool & WriteFileTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Why:** Enable file operations - read code, write reports, manage documents.

**Integration Time:** 15 minutes for both

**Use Case:** Work with local files through the chatbot.

**Example:** "Read config.json and explain it" or "Save this conversation to a file"

**Code Snippet:**
```python
from langchain_community.tools.file_management import ReadFileTool, WriteFileTool

read_tool = ReadFileTool()
write_tool = WriteFileTool()
```

---

#### 8. JsonGetValueTool & JsonListKeysTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Why:** Parse JSON responses from APIs or user inputs. Very useful with your stock tool.

**Integration Time:** 10 minutes for both

**Use Case:** Extract and analyze JSON data.

**Example:** Parse complex JSON responses from APIs and extract specific values.

**Code Snippet:**
```python
from langchain_community.tools.json.tool import JsonGetValueTool, JsonListKeysTool

json_get_tool = JsonGetValueTool()
json_list_tool = JsonListKeysTool()
```

---

#### 9. RequestsGetTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Why:** Make HTTP requests to any API. Extremely versatile for integrations.

**Integration Time:** 15 minutes

**Use Case:** Fetch data from any REST API endpoint.

**Example:** Query any public API for data, news, or information.

**Code Snippet:**
```python
from langchain_community.tools.requests.tool import RequestsGetTool

requests_tool = RequestsGetTool()
```

---

#### 10. PolygonLastQuote & PolygonTickerNews
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Why:** Enhance your stock tool with real-time quotes and news. Free tier available.

**Integration Time:** 20 minutes each

**Use Case:** Get real-time stock quotes and company news.

**Example:** "What's the current quote for TSLA?" → Bid/ask prices and latest news.

**Code Snippet:**
```python
from langchain_community.tools.polygon import PolygonLastQuote, PolygonTickerNews

polygon_quote = PolygonLastQuote()
polygon_news = PolygonTickerNews()
```

---

### Tier 3: Nice-to-Have Tools

#### 11. StackExchangeTool
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Why:** Find programming solutions from Stack Overflow.

**Integration Time:** 15 minutes

**Example:** "How to fix Python import error?" → Stack Overflow solutions.

---

#### 12. RedditSearchRun
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Why:** Search Reddit for discussions and community opinions.

**Integration Time:** 15 minutes

**Example:** "What do people say about GPT-4 on Reddit?" → Reddit discussions.

---

#### 13. NasaAction
**Tags:** 🆓 Free/Open Source | 🟢 Low Effort

**Why:** Access NASA data, space images, and mission information.

**Integration Time:** 15 minutes

**Example:** "Show me Mars rover images" → NASA API data and images.

---

#### 14. GoogleBooksQueryRun
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Why:** Find books and reading recommendations.

**Integration Time:** 20 minutes

**Example:** "Find books about machine learning" → Book recommendations with details.

---

#### 15. IFTTTWebhook
**Tags:** 🎁 Free Tier | 🟢 Low Effort

**Why:** Trigger IFTTT automations for smart home, notifications, etc.

**Integration Time:** 20 minutes

**Example:** "Turn on my lights" → Triggers IFTTT webhook to control smart lights.

---

### Implementation Priority

**Week 1 - Essential Tools (Total: ~2 hours)**
1. WikipediaQueryRun (15 min)
2. YahooFinanceNewsTool (10 min)
3. ArxivQueryRun (15 min)
4. YouTubeSearchTool (15 min)
5. OpenWeatherMapQueryRun (20 min)
6. JsonGetValueTool & JsonListKeysTool (10 min)

**Week 2 - Enhanced Functionality (Total: ~1.5 hours)**
1. WolframAlphaQueryRun (20 min)
2. ReadFileTool & WriteFileTool (15 min)
3. RequestsGetTool (15 min)
4. PolygonLastQuote (20 min)
5. PolygonTickerNews (20 min)

**Week 3 - Additional Features (Total: ~1 hour)**
1. StackExchangeTool (15 min)
2. RedditSearchRun (15 min)
3. NasaAction (15 min)
4. GoogleBooksQueryRun (20 min)

---

### Quick Integration Template

Here's how to add these tools to your existing `backend_with_tool.py`:

```python
# Add these imports
from langchain_community.tools import (
    WikipediaQueryRun,
    OpenWeatherMapQueryRun,
    YahooFinanceNewsTool,
    ArxivQueryRun,
    YouTubeSearchTool,
    WolframAlphaQueryRun,
)
from langchain_community.utilities import (
    WikipediaAPIWrapper,
    OpenWeatherMapAPIWrapper,
    WolframAlphaAPIWrapper,
    ArxivAPIWrapper,
)

# Initialize tools
wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
weather_tool = OpenWeatherMapQueryRun(api_wrapper=OpenWeatherMapAPIWrapper())
finance_news_tool = YahooFinanceNewsTool()
arxiv_tool = ArxivQueryRun(api_wrapper=ArxivAPIWrapper())
youtube_tool = YouTubeSearchTool()
wolfram_tool = WolframAlphaQueryRun(api_wrapper=WolframAlphaAPIWrapper())

# Update your tools list
tools = [
    search_tool, 
    calculator, 
    get_stock_price,
    wikipedia_tool,
    weather_tool,
    finance_news_tool,
    arxiv_tool,
    youtube_tool,
    wolfram_tool,
]
```

---

### Environment Variables Needed

Add these to your `.env` file:

```env
# Already have
ALPHA_VANTAGE_API_KEY=your_key_here

# New tools
OPENWEATHERMAP_API_KEY=your_key_here
WOLFRAM_ALPHA_APPID=your_key_here
POLYGON_API_KEY=your_key_here  # Optional, if using Polygon tools
```

---

### Summary

**Recommended Count:** 15 tools total

**Free/Open Source:** 9 tools (60%)
**Free Tier:** 6 tools (40%)
**Paid:** 0 tools (0%)

**Low Effort:** 14 tools (93%)
**Medium Effort:** 1 tool (7%)
**High Effort:** 0 tools (0%)

**Total Implementation Time:** ~4-5 hours spread over 2-3 weeks

All recommended tools are either completely free or have generous free tiers that will work well for your chatbot use case!

---

*Generated for LangGraph Chatbot Project - December 2025*
