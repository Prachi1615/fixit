import React, { useState } from "react";
import { motion } from "framer-motion";
import { useStytch, useStytchUser } from "@stytch/nextjs";
import { useRouter } from "next/router";

const Profile = () => {
  const [inputType, setInputType] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);
  const stytch = useStytch();
  const { user } = useStytchUser();
  const router = useRouter();

  const handleLogout = () => {
    stytch.session.revoke();
    router.push("/");
  };

  const handleInputTypeSelect = (type) => {
    setInputType(type);
    setResponse(null);
    setError(null);
  };

  const handleSubmit = async () => {
    if (!inputType) {
      setError("Please select an input type.");
      return;
    }

    setIsLoading(true);
    setError(null);
    setResponse(null);

    try {
      const res = await fetch("/process_input", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input_type: inputType }),
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.message || "Failed to process input");

      setResponse(data.result);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-8">
      <motion.div 
        initial={{ opacity: 0, y: 20 }} 
        animate={{ opacity: 1, y: 0 }} 
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="w-full max-w-3xl bg-black/20 backdrop-blur-xl shadow-2xl rounded-3xl p-12 space-y-8 border border-white/10"
      >
        <div className="flex justify-between items-center">
          <div>
            <h2 className="text-4xl font-extrabold text-white">Welcome!</h2>
            <p className="text-white/80 mt-2">{user?.emails[0]?.email}</p>
          </div>
          <motion.button
            onClick={handleLogout}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="px-6 py-3 bg-white/10 hover:bg-white/20 text-white rounded-xl shadow-lg backdrop-blur-sm transition-all text-base font-bold"
          >
            Logout
          </motion.button>
        </div>

        <div className="pt-4">
          <h3 className="text-2xl font-bold text-white text-center mb-8">Select Input Type</h3>

          <div className="flex flex-wrap justify-center gap-6">
            {["text", "image", "audio", "video"].map((type) => (
              <motion.button
                key={type}
                whileHover={{ scale: 1.05, y: -5 }}
                whileTap={{ scale: 0.95 }}
                className={`px-8 py-5 text-xl font-bold rounded-2xl transition-all shadow-lg backdrop-blur-sm
                  ${inputType === type 
                    ? "bg-gradient-to-r from-[#00CCCC] to-[#b169a6] text-white shadow-[#00CCCC]/25" 
                    : "bg-white/10 text-white hover:bg-white/20 shadow-white/10"}`}
                onClick={() => handleInputTypeSelect(type)}
              >
                {type.toUpperCase()}
              </motion.button>
            ))}
          </div>

          <motion.button
            onClick={handleSubmit}
            disabled={isLoading}
            whileHover={{ scale: 1.05, y: -5 }}
            whileTap={{ scale: 0.95 }}
            className="w-full py-5 bg-gradient-to-r from-[#00CCCC] to-[#b169a6] hover:from-[#00CCCC] hover:to-[#cf8cc4] text-white rounded-2xl shadow-lg shadow-[#00CCCC]/25 transition-all text-xl font-bold disabled:opacity-50 disabled:cursor-not-allowed backdrop-blur-sm"
          >
            {isLoading ? "Processing..." : "Submit"}
          </motion.button>

          {response && (
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              className="p-6 bg-[#1E293B] text-white rounded-xl border border-[#334155] mt-4"
            >
              <h3 className="text-2xl font-semibold">Response:</h3>
              <p className="text-lg">{JSON.stringify(response, null, 2)}</p>
            </motion.div>
          )}

          {error && (
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              className="p-6 bg-red-700 text-white rounded-xl border border-red-900 mt-4"
            >
              <p>{error}</p>
            </motion.div>
          )}
        </div>
      </motion.div>
    </div>
  );
};

export default Profile;
