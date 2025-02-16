import { Html, Head, Main, NextScript } from "next/document";
import Image from "next/image";
import Link from "next/link";

export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <body className="flex flex-col items-center justify-center min-h-screen">
        <h2 className="text-3xl font-bold text-center mb-8">FIXIT</h2>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
