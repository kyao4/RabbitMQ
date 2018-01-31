package hw1;

import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.AMQP;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Consumer;
import com.rabbitmq.client.DefaultConsumer;
import com.rabbitmq.client.Envelope;

import java.io.IOException;
import java.util.concurrent.TimeoutException;


public class Recv {
	private final static String QUEUE_NAME = "HelloJava";
	public static void main(String[] args) throws java.io.IOException, TimeoutException {
		ConnectionFactory factory = new ConnectionFactory();
		factory.setHost("localhost");
		Connection conn = factory.newConnection();
		Channel channel = conn.createChannel();
		channel.queueDeclare(QUEUE_NAME, false, false, false, null);
		System.out.println("[*] Waiting for messages. To exit press CTRL+C");
		Consumer consumer = new DefaultConsumer(channel) {
			@Override
			  public void handleDelivery(String consumerTag, Envelope envelope,
			                             AMQP.BasicProperties properties, byte[] body)
			      throws IOException {
				String message = new String(body, "UTF-8");
				System.out.println("[X] Received message '" + message + "'");
			}
		};
		
		channel.basicConsume(QUEUE_NAME, true, consumer);
	}
	
	
}
