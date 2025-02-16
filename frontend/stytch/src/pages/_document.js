import { Html, Head, Main, NextScript } from 'next/document';

export default function Document() {
  return (
    <Html lang="en">
      <Head>
        <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
        <style>{`
          body {
            font-family: 'Space Grotesk', sans-serif;
          }
          
          .gradient-bg {
            background: linear-gradient(-45deg, #00CCCC, #b169a6);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
          }
          
          @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
          }
        `}</style>
      </Head>
      <body className="gradient-bg min-h-screen">
        <div className="flex flex-col items-center justify-start min-h-screen p-8">
          <h1 className="text-7xl font-bold text-white mb-16 mt-12 tracking-tight text-center">FIXIT</h1>
          <Main />
          <NextScript />
        </div>
      </body>
    </Html>
  );
}
