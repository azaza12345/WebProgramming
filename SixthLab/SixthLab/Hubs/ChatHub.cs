using System;
using System.Threading.Tasks;
using Microsoft.AspNetCore.SignalR;

namespace SixthLab.Hubs
{
    public class ChatHub : Hub
    {
        public async Task Send(string message, string userName)
        {
            await Clients.All.SendAsync("Send", message, userName);
        }
    }
}