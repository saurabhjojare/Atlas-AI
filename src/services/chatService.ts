import { sendMessageApi } from "../api/chatApi";

export const sendChatMessage = async (
  message: string
): Promise<string> => {

  const response = await sendMessageApi({
    message,
  });

  return response.response;
};