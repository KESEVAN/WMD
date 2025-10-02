# Deep Research App

## Mission

To provide a simple, elegant, and powerful tool for deep multi-agent research, enabling users to gain insights from a variety of sources in a clean and modular way.

## Features

*   **Multi-Agent Research**: Utilizes a multi-agent approach inspired by Anthropic to break down complex queries, perform parallel research, and synthesize findings.
*   **Modern UI**: A clean and intuitive user interface built with Next.js and Tailwind CSS for a seamless user experience.
*   **Modular Backend**: A robust backend powered by FastAPI, ensuring a scalable and maintainable architecture.

## Technology Stack

### Backend

*   **[FastAPI](https://fastapi.tiangolo.com/)**: A modern, fast (high-performance), web framework for building APIs with Python.
*   **[Cerebras](https://www.cerebras.net/)**: Used for generating AI-powered insights and analysis.
*   **[Exa](https://exa.ai/)**: Powers the web search capabilities of the research agents.

### Frontend

*   **[Next.js](https://nextjs.org/)**: A React framework for building user interfaces.
*   **[React](https://reactjs.org/)**: A JavaScript library for building user interfaces.
*   **[Tailwind CSS](https://tailwindcss.com/)**: A utility-first CSS framework for rapid UI development.

## Future Integrations

We are constantly looking to expand the capabilities of the Deep Research App. Here are some of the future integrations we are exploring:

*   **[OpenRouter](https://openrouter.ai/)**: To provide access to a wider range of language models and enhance the research capabilities of the agents.
*   **[Llama Agents MCP](https://github.com/run-llama/llama-agents)**: To explore more advanced and complex multi-agent collaboration patterns and workflows.

* Soon to be deployed on Netlify.

## Getting Started

### Prerequisites

*   [Python 3.8+](https://www.python.org/downloads/)
*   [Node.js 14.x+](https://nodejs.org/en/download/)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/deep-research-app.git
    cd deep-research-app
    ```

2.  **Backend Setup:**

    ```bash
    cd backend
    pip install -r requirements.txt
    ```

3.  **Frontend Setup:**

    ```bash
    cd ../frontend
    npm install
    ```

### Running the Application

1.  **Add your API keys:**

    Rename `.env.example` to `.env` in the `backend` directory and add your API keys for Cerebras and Exa.

2.  **Start the backend server:**

    ```bash
    cd backend
    uvicorn app.main:app --reload
    ```

3.  **Start the frontend server:**

    ```bash
    cd ../frontend
    npm run dev
    ```

4.  Open your browser and navigate to `http://localhost:3000`.
