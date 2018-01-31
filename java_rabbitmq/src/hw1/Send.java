package hw1;

import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.Channel;
import java.util.concurrent.TimeoutException;





public class Send {

	private final static String QUEUE_NAME = "HelloJava";
	
	public static void main(String[] args) throws java.io.IOException, TimeoutException {
		ConnectionFactory factory = new ConnectionFactory();
		factory.setHost("localhost");
		Connection conn = factory.newConnection();
		Channel channel = conn.createChannel();
		channel.queueDeclare(QUEUE_NAME, false, false, false, null);
		String message = "Hello World in Java!";
		channel.basicPublish("", QUEUE_NAME, null, message.getBytes());
		System.out.println("[X] Sent " + message + "!");
		channel.close();
		conn.close();
	}
	
	
}
